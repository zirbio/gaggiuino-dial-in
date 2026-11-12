import unittest
from typing import Any

import server

BEANS = [
    {"id": 1, "name": "Timbuyacu"},
    {"id": 2, "name": "Churupallana"},
    {"id": 3, "name": "Descafeinado Chambakú"},
]


class FakeClient:
    def __init__(self) -> None:
        self.annotated: list[tuple[int, dict[str, Any]]] = []
        self.shots = {
            650: {"id": 650, "timestamp": 1794231270, "duration": 372},
            649: {"id": 649, "timestamp": 1794210000, "duration": 471},
        }

    def beans(self) -> list[dict[str, Any]]:
        return BEANS

    def latest_shot(self) -> dict[str, Any] | None:
        return self.shots[650]

    def shot(self, shot_id: int) -> dict[str, Any] | None:
        return self.shots.get(shot_id)

    def annotate(self, shot_id: int, fields: dict[str, Any]) -> dict[str, Any]:
        self.annotated.append((shot_id, fields))
        return {"ok": True}


def call(client: FakeClient, arguments: dict[str, Any]) -> dict[str, Any]:
    response = server.handle_rpc(
        {"jsonrpc": "2.0", "id": 7, "method": "tools/call",
         "params": {"name": "assign_shot_coffee", "arguments": arguments}},
        client,  # type: ignore[arg-type]
    )
    assert response is not None
    return response["result"]


class MatchBeanTest(unittest.TestCase):
    def test_accent_and_case_insensitive_partial(self) -> None:
        self.assertEqual(server.match_bean("chambaku", BEANS)["id"], 3)

    def test_exact_name_wins(self) -> None:
        beans = BEANS + [{"id": 4, "name": "Timbuyacu Reserva"}]
        self.assertEqual(server.match_bean("timbuyacu", beans)["id"], 1)

    def test_ambiguous_raises(self) -> None:
        beans = [{"id": 1, "name": "Etiopía Guji"}, {"id": 2, "name": "Etiopía Sidamo"}]
        with self.assertRaisesRegex(server.ToolError, "varios"):
            server.match_bean("etiopia", beans)

    def test_unknown_lists_available(self) -> None:
        with self.assertRaisesRegex(server.ToolError, "Timbuyacu"):
            server.match_bean("kenia", BEANS)


class AssignToolTest(unittest.TestCase):
    def test_defaults_to_latest_shot_and_sets_bean_and_dose(self) -> None:
        client = FakeClient()
        result = call(client, {"coffee": "timbuyacu", "dose_g": 18})
        self.assertFalse(result["isError"])
        self.assertEqual(client.annotated, [(650, {"beanId": 1, "coffee": "Timbuyacu", "dose": 18.0})])
        self.assertIn("09/11/2026 14:34", result["content"][0]["text"])
        self.assertIn("37,2 s", result["content"][0]["text"])

    def test_without_dose_keeps_stored_dose(self) -> None:
        client = FakeClient()
        call(client, {"coffee": "churupallana", "shot_id": 649})
        self.assertEqual(client.annotated, [(649, {"beanId": 2, "coffee": "Churupallana"})])

    def test_rejects_out_of_range_dose_without_writing(self) -> None:
        client = FakeClient()
        result = call(client, {"coffee": "timbuyacu", "dose_g": 180})
        self.assertTrue(result["isError"])
        self.assertEqual(client.annotated, [])

    def test_unknown_shot_is_an_error(self) -> None:
        client = FakeClient()
        result = call(client, {"coffee": "timbuyacu", "shot_id": 9999})
        self.assertTrue(result["isError"])
        self.assertEqual(client.annotated, [])


class ProtocolTest(unittest.TestCase):
    def test_initialize_echoes_supported_version(self) -> None:
        response = server.handle_rpc(
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-03-26"}},
            FakeClient(),  # type: ignore[arg-type]
        )
        assert response is not None
        self.assertEqual(response["result"]["protocolVersion"], "2025-03-26")

    def test_notification_has_no_response(self) -> None:
        response = server.handle_rpc(
            {"jsonrpc": "2.0", "method": "notifications/initialized"}, FakeClient()  # type: ignore[arg-type]
        )
        self.assertIsNone(response)

    def test_lists_only_the_assign_tool_without_machine(self) -> None:
        response = server.handle_rpc(
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}, FakeClient()  # type: ignore[arg-type]
        )
        assert response is not None
        self.assertEqual([t["name"] for t in response["result"]["tools"]], ["assign_shot_coffee"])

    def test_lists_machine_tools_when_configured(self) -> None:
        response = server.handle_rpc(
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            FakeClient(), FakeMachine(),  # type: ignore[arg-type]
        )
        assert response is not None
        tools = response["result"]["tools"]
        self.assertEqual(
            [t["name"] for t in tools],
            ["assign_shot_coffee", "get_shot_profile", "list_machine_profiles"],
        )
        self.assertTrue(all(t["annotations"]["readOnlyHint"] for t in tools[1:]))

    def test_machine_tool_unknown_without_machine(self) -> None:
        response = server.handle_rpc(
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
             "params": {"name": "get_shot_profile", "arguments": {}}},
            FakeClient(),  # type: ignore[arg-type]
        )
        assert response is not None
        self.assertEqual(response["error"]["code"], -32602)


LONDINIUM = {
    "name": "Londinium",
    "waterTemperature": 92,
    "globalStopConditions": {"weight": 40},
    "recipe": {"coffeeIn": 20, "ratio": 2},
    "phases": [
        {"type": "FLOW", "target": {"end": 9, "curve": "INSTANT"}, "restriction": 4,
         "stopConditions": {"time": 10000, "pressureAbove": 4, "waterPumpedInPhase": 65}},
        {"type": "FLOW", "target": {"end": 0, "curve": "INSTANT"},
         "stopConditions": {"time": 10000, "pressureBelow": 0.7}},
        {"type": "PRESSURE", "target": {"start": 9, "end": 3, "curve": "EASE_IN_OUT", "time": 20000},
         "restriction": 3, "stopConditions": {}},
    ],
}


class FakeMachine:
    def __init__(self) -> None:
        self.shots = {654: {"id": 654, "timestamp": 1794376122, "duration": 422, "profile": LONDINIUM}}

    def latest_shot_id(self) -> int:
        return 654

    def shot(self, shot_id: int) -> dict[str, Any]:
        if shot_id not in self.shots:
            raise server.ToolError(f"No existe el shot {shot_id} en la Gaggiuino.")
        return self.shots[shot_id]

    def profiles(self) -> list[dict[str, Any]]:
        return [
            {"id": 1, "name": "IUIUIU Classic", "selected": "true"},
            {"id": 14, "name": "Leva 9 v0.9 (community)", "selected": "false"},
        ]


def call_machine(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    response = server.handle_rpc(
        {"jsonrpc": "2.0", "id": 9, "method": "tools/call", "params": {"name": name, "arguments": arguments}},
        FakeClient(), FakeMachine(),  # type: ignore[arg-type]
    )
    assert response is not None
    return response["result"]


class MachineToolsTest(unittest.TestCase):
    def test_shot_profile_defaults_to_latest(self) -> None:
        result = call_machine("get_shot_profile", {})
        self.assertFalse(result["isError"])
        text = result["content"][0]["text"]
        self.assertIn("Shot #654 (11/11/2026 06:48, 42,2 s)", text)
        self.assertIn("Perfil: Londinium", text)
        self.assertIn("Para en: 40 g", text)
        self.assertIn("1. flujo 9 ml/s, límite 4 bar; termina con 10 s o presión > 4 bar o 65 ml bombeados", text)
        self.assertIn("2. flujo 0 ml/s; termina con 10 s o presión < 0,7 bar", text)
        self.assertIn("3. presión 9 → 3 bar en 20 s (EASE_IN_OUT), límite 3 ml/s; hasta el final del shot", text)

    def test_shot_profile_without_weight_stop_says_so(self) -> None:
        profile = dict(LONDINIUM, globalStopConditions={"weight": 0})
        text = "\n".join(server.describe_profile(profile))
        self.assertIn("sin stop-on-weight", text)

    def test_unknown_shot_is_an_error(self) -> None:
        result = call_machine("get_shot_profile", {"shot_id": 1})
        self.assertTrue(result["isError"])

    def test_rejects_non_integer_shot_id(self) -> None:
        result = call_machine("get_shot_profile", {"shot_id": "654"})
        self.assertTrue(result["isError"])

    def test_lists_profiles_and_marks_active(self) -> None:
        text = call_machine("list_machine_profiles", {})["content"][0]["text"]
        self.assertIn("- IUIUIU Classic (activo)", text)
        self.assertIn("- Leva 9 v0.9 (community)\n", text + "\n")


if __name__ == "__main__":
    unittest.main()
