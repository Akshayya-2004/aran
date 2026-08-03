import json

from app.schemas import AnalysisResult


def parse_response(response_text: str) -> AnalysisResult:

    response_text = response_text.strip()

    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()

    data = json.loads(response_text)

    return AnalysisResult(**data)