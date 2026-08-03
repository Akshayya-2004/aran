from app.models import User
from app.repositories import (
    ReportRepository,
    EvidenceRepository,
)
from app.schemas import ReportCreate
from app.services.ai_service import AIService
from app.services.evidence_service import EvidenceService
from app.services.report_service import ReportService


class ReportWorkflowService:

    def __init__(
        self,
        report_repository: ReportRepository,
        evidence_repository: EvidenceRepository,
    ):
        self.ai_service = AIService()

        self.report_service = ReportService(
            report_repository
        )

        self.evidence_service = EvidenceService(
            evidence_repository
        )

    def create_report(
        self,
        report_data: ReportCreate,
        current_user: User,
    ):

        analysis = self.ai_service.analyze(
            report_data.selected_text
        )

        report = self.report_service.create_report(
            report_data,
            current_user,
            analysis,
        )

        self.evidence_service.generate_evidence(
            report
        )

        return report