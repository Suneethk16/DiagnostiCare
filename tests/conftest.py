import pytest


@pytest.fixture
def mock_call_gemini(monkeypatch):
    def fake_llm(prompt):
        return """
        {
          "diagnosis": "Diabetes",
          "medications": ["Metformin"],
          "lab_results": ["HbA1c 8.2%"],
          "doctor_instructions": ["Repeat test"]
        }
        """

    monkeypatch.setattr(
        "agents.document_agent.call_gemini",
        fake_llm
    )
