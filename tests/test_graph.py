from graph_orchestrator import build_graph


def test_graph_runs(mock_call_gemini):

    graph = build_graph()

    result = graph.invoke({
        "report_text": "Patient with diabetes",
        "document": None,
        "reasoning": None,
        "actions": None,
        "safety": None
    })

    assert "document" in result
