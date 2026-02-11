import json
from schemas.medical_schemas import ActionPlan
from utils.gemini_client import call_gemini
from utils.prompt_templates import ACTION_PROMPT

def action_agent(reasoning) -> ActionPlan:
    prompt = ACTION_PROMPT + "\n\nClinical Reasoning:\n" + reasoning.model_dump_json()
    raw_output = call_gemini(prompt)
    
    # Remove markdown code blocks if present
    raw_output = raw_output.strip()
    if raw_output.startswith("```json"):
        raw_output = raw_output[7:]
    if raw_output.startswith("```"):
        raw_output = raw_output[3:]
    if raw_output.endswith("```"):
        raw_output = raw_output[:-3]
    raw_output = raw_output.strip()

    data = json.loads(raw_output)
    return ActionPlan(**data)
