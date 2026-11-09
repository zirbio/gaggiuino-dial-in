"""Servidor MCP mínimo que permite a un asistente asignar café y dosis a un shot de GLP.

El MCP de GLP 3.7.0 solo deja cambiar puntuación, notas y molienda. Este puente
añade una única herramienta, ``assign_shot_coffee``, que liga el shot a un café
de la biblioteca (para que GLP descuente stock y lo cuente en sus estadísticas)
y opcionalmente fija la dosis. No toca nada más.

Solo usa la biblioteca estándar. Configuración por entorno:
  GLP_URL    URL base de GLP (por defecto http://glp:8099)
  GLP_TOKEN  token de la API de GLP (obligatorio)
  PORT       puerto de escucha (por defecto 8200)
"""

from __future__ import annotations

import datetime
import json
import os
import sys
import unicodedata
import urllib.error
import urllib.request
import zoneinfo
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

SERVER_NAME = "glp-grok-bridge"
SERVER_VERSION = "1.0.0"
SUPPORTED_PROTOCOLS = ("2025-06-18", "2025-03-26", "2024-11-05")
LOCAL_TZ = zoneinfo.ZoneInfo("Europe/Madrid")
MIN_DOSE_G = 5.0
MAX_DOSE_G = 30.0

ASSIGN_TOOL = {
    "name": "assign_shot_coffee",
    "title": "Assign coffee to shot",
    "description": (
        "Record which coffee (bean from the user's GLP library) and, optionally, which dose in "
        "grams was used for an espresso shot. Linking the bean makes GLP deduct it from the bag's "
        "stock and count the shot in that bean's statistics. Omit shot_id to use the most recent "
        "shot. The coffee name is matched against the library ignoring case and accents, and a "
        "unique part of the name is enough (e.g. 'chambaku'). Use GLP's annotate_shot for rating, "
        "notes and grind setting."
    ),
    "inputSchema": {
        "type": "object",
        "properties": {
            "coffee": {
                "type": "string",
                "description": "Coffee name or a unique part of it, as it appears in the GLP library",
            },
            "shot_id": {
                "type": "integer",
                "description": "Shot id from list_shots; omit for the most recent shot",
            },
            "dose_g": {
                "type": "number",
                "description": f"Ground coffee dose in grams ({MIN_DOSE_G:g}-{MAX_DOSE_G:g}); omit to keep the stored dose",
            },
        },
        "required": ["coffee"],
        "additionalProperties": False,
    },
    "annotations": {
        "title": "Assign coffee to shot",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
}


class ToolError(Exception):
    """Error que se devuelve al asistente como resultado de la herramienta."""


class GlpClient:
    def __init__(self, base_url: str, token: str, timeout: float = 15.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout

    def _request(self, method: str, path: str, body: dict[str, Any] | None = None) -> Any:
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(
            self.base_url + path,
            data=data,
            method=method,
            headers={"X-GLP-Token": self.token, "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            raise ToolError(f"GLP respondió {exc.code} en {method} {path}") from exc
        except urllib.error.URLError as exc:
            raise ToolError(f"No se pudo conectar con GLP: {exc.reason}") from exc

    def beans(self) -> list[dict[str, Any]]:
        return list(self._request("GET", "/api/library").get("beans") or [])

    def latest_shot(self) -> dict[str, Any] | None:
        shots = self._request("GET", "/api/shots?limit=1").get("shots") or []
        return shots[0] if shots else None

    def shot(self, shot_id: int) -> dict[str, Any] | None:
        return self._request("GET", f"/api/shots/{shot_id}")

    def annotate(self, shot_id: int, fields: dict[str, Any]) -> dict[str, Any]:
        return self._request("POST", f"/api/shots/{shot_id}/annotate", fields)


def normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    return " ".join("".join(c for c in decomposed if not unicodedata.combining(c)).lower().split())


def match_bean(query: str, beans: list[dict[str, Any]]) -> dict[str, Any]:
    wanted = normalize(query)
    if not wanted:
        raise ToolError("Indica el nombre del café.")
    names = ", ".join(str(b.get("name")) for b in beans) or "(biblioteca vacía)"
    exact = [b for b in beans if normalize(str(b.get("name", ""))) == wanted]
    if len(exact) == 1:
        return exact[0]
    partial = [b for b in beans if wanted in normalize(str(b.get("name", "")))]
    if len(partial) == 1:
        return partial[0]
    if not partial:
        raise ToolError(f"No hay ningún café que coincida con «{query}». Cafés disponibles: {names}.")
    options = ", ".join(str(b.get("name")) for b in partial)
    raise ToolError(f"«{query}» coincide con varios cafés ({options}). Indica cuál.")


def format_local_time(timestamp: Any) -> str:
    if not isinstance(timestamp, (int, float)):
        return "hora desconocida"
    seconds = timestamp / 1000 if timestamp > 10**11 else timestamp
    return datetime.datetime.fromtimestamp(seconds, LOCAL_TZ).strftime("%d/%m/%Y %H:%M")


def format_number(value: float) -> str:
    return f"{value:.1f}".rstrip("0").rstrip(".").replace(".", ",")


def assign_shot_coffee(client: GlpClient, args: dict[str, Any]) -> str:
    coffee = args.get("coffee")
    if not isinstance(coffee, str):
        raise ToolError("El parámetro coffee es obligatorio.")
    dose = args.get("dose_g")
    if dose is not None:
        if isinstance(dose, bool) or not isinstance(dose, (int, float)):
            raise ToolError("dose_g debe ser un número de gramos.")
        if not MIN_DOSE_G <= dose <= MAX_DOSE_G:
            raise ToolError(f"La dosis debe estar entre {MIN_DOSE_G:g} y {MAX_DOSE_G:g} g.")

    shot_id = args.get("shot_id")
    if shot_id is None:
        shot = client.latest_shot()
        if not shot:
            raise ToolError("GLP todavía no tiene ningún shot.")
    else:
        if isinstance(shot_id, bool) or not isinstance(shot_id, int):
            raise ToolError("shot_id debe ser un número entero.")
        shot = client.shot(shot_id)
        if not shot:
            raise ToolError(f"No existe el shot {shot_id} en GLP.")

    bean = match_bean(coffee, client.beans())
    fields: dict[str, Any] = {"beanId": bean["id"], "coffee": bean["name"]}
    if dose is not None:
        fields["dose"] = round(float(dose), 1)
    client.annotate(int(shot["id"]), fields)

    parts = [f"Shot #{shot['id']} ({format_local_time(shot.get('timestamp'))}"]
    duration = shot.get("duration")
    if isinstance(duration, (int, float)) and duration > 0:
        parts.append(f", {format_number(duration / 10)} s")
    parts.append(f") anotado con {bean['name']}")
    if dose is not None:
        parts.append(f", dosis {format_number(float(dose))} g")
    return "".join(parts) + "."


def handle_rpc(message: Any, client: GlpClient) -> dict[str, Any] | None:
    if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
        return _error(None, -32600, "Invalid Request")
    method = message.get("method")
    msg_id = message.get("id")
    if msg_id is None:
        return None  # notificación: no lleva respuesta
    params = message.get("params") or {}

    if method == "initialize":
        requested = params.get("protocolVersion")
        version = requested if requested in SUPPORTED_PROTOCOLS else SUPPORTED_PROTOCOLS[0]
        return _result(msg_id, {
            "protocolVersion": version,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
            "instructions": "Assigns a coffee from the GLP library (and optionally the dose) to an espresso shot.",
        })
    if method == "ping":
        return _result(msg_id, {})
    if method == "tools/list":
        return _result(msg_id, {"tools": [ASSIGN_TOOL]})
    if method == "tools/call":
        if params.get("name") != ASSIGN_TOOL["name"]:
            return _error(msg_id, -32602, f"Unknown tool: {params.get('name')}")
        try:
            text = assign_shot_coffee(client, params.get("arguments") or {})
            return _result(msg_id, {"content": [{"type": "text", "text": text}], "isError": False})
        except ToolError as exc:
            return _result(msg_id, {"content": [{"type": "text", "text": str(exc)}], "isError": True})
    return _error(msg_id, -32601, f"Method not found: {method}")


def _result(msg_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": msg_id, "result": result}


def _error(msg_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": code, "message": message}}


def make_handler(client: GlpClient) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        server_version = SERVER_NAME

        def do_POST(self) -> None:  # noqa: N802 (nombre impuesto por http.server)
            if self.path.split("?")[0] != "/mcp":
                self._send(404, None)
                return
            length = int(self.headers.get("Content-Length") or 0)
            if length <= 0 or length > 1_000_000:
                self._send(400, _error(None, -32700, "Parse error"))
                return
            try:
                message = json.loads(self.rfile.read(length))
            except json.JSONDecodeError:
                self._send(400, _error(None, -32700, "Parse error"))
                return
            if isinstance(message, list):
                self._send(400, _error(None, -32600, "Batch requests are not supported"))
                return
            response = handle_rpc(message, client)
            if response is None:
                self._send(202, None)
            else:
                self._send(200, response)

        def do_GET(self) -> None:  # noqa: N802
            self._send(405, None)

        def do_DELETE(self) -> None:  # noqa: N802
            self._send(405, None)

        def _send(self, status: int, payload: dict[str, Any] | None) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode() if payload is not None else b""
            self.send_response(status)
            if payload is not None:
                self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if body:
                self.wfile.write(body)

        def log_message(self, fmt: str, *args: Any) -> None:
            sys.stderr.write(f"{self.address_string()} {fmt % args}\n")

    return Handler


def main() -> None:
    token = os.environ.get("GLP_TOKEN", "")
    if not token:
        sys.exit("GLP_TOKEN es obligatorio")
    client = GlpClient(os.environ.get("GLP_URL", "http://glp:8099"), token)
    port = int(os.environ.get("PORT", "8200"))
    ThreadingHTTPServer(("0.0.0.0", port), make_handler(client)).serve_forever()


if __name__ == "__main__":
    main()
