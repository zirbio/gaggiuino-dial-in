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

    def test_lists_only_the_assign_tool(self) -> None:
        response = server.handle_rpc(
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}, FakeClient()  # type: ignore[arg-type]
        )
        assert response is not None
        self.assertEqual([t["name"] for t in response["result"]["tools"]], ["assign_shot_coffee"])


if __name__ == "__main__":
    unittest.main()
