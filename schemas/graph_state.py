from typing import TypedDict, Optional
from schemas.medical_schemas import (
    DocumentExtraction,
    ClinicalReasoning,
    ActionPlan,
    SafetyReview
)


class AgentState(TypedDict):
    report_text: str
    document: Optional[DocumentExtraction]
    reasoning: Optional[ClinicalReasoning]
    actions: Optional[ActionPlan]
    safety: Optional[SafetyReview]
