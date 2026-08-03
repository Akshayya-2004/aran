from google import genai

from app.ai.prompt_builder import build_prompt
from app.ai.response_parser import parse_response
from app.core.config import settings
from app.schemas import AnalysisResult


class AIService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def analyze(
        self,
        text: str,
    ) -> AnalysisResult:

        prompt = build_prompt(text)

        response = self.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
        )

        return parse_response(
            response.text
        )