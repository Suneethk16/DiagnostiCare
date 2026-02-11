from pydantic import BaseModel, Field
from typing import List, Optional


class DocumentExtraction(BaseModel):
    diagnosis: str
    medications: List[str]
    lab_results: List[str]
    doctor_instructions: List[str]


class ClinicalReasoning(BaseModel):
    critical_findings: List[str]
    required_actions: List[str]
    missing_information: List[str]


class ActionPlan(BaseModel):
    actions: List[str]


class SafetyReview(BaseModel):
    doctor_confirmation_required: List[str]
    high_risk_actions: List[str]
