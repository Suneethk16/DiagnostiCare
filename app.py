from utils.file_loader import load_medical_report
from agents.document_agent import document_agent
from agents.reasoning_agent import reasoning_agent
from agents.action_agent import action_agent
from agents.safety_agent import safety_agent

report = load_medical_report("data/sample_report.txt")

doc = document_agent(report)
print("\n--- Document Agent (JSON) ---")
print(doc.model_dump_json(indent=2))

reasoning = reasoning_agent(doc)
print("\n--- Reasoning Agent (JSON) ---")
print(reasoning.model_dump_json(indent=2))

actions = action_agent(reasoning)
print("\n--- Action Agent (JSON) ---")
print(actions.model_dump_json(indent=2))

safety = safety_agent(actions)
print("\n--- Safety Agent (JSON) ---")
print(safety.model_dump_json(indent=2))
