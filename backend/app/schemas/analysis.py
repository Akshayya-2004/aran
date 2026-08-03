from pydantic import BaseModel

from app.enums import Severity


class AnalysisResult(BaseModel):
    classification: str
    severity: Severity
    confidence: float
    language: str
    explanation: str