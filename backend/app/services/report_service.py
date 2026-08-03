import random
from datetime import datetime
from typing import Any

from app.enums import ReportStatus, Severity
from app.models import Report, User
from app.repositories import ReportRepository
from app.schemas import ReportCreate
from app.repositories.evidence_repository import EvidenceRepository
from app.services.evidence_service import EvidenceService
from app.schemas import AnalysisResult

class ReportService:

    def __init__(self, repository: ReportRepository):
        self.repository = repository

    def _generate_case_id(self) -> str:
        """
        Example:
        ARAN-20260729-483921
        """
        date = datetime.now().strftime("%Y%m%d")
        unique = random.randint(100000, 999999)

        return f"ARAN-{date}-{unique}"

    def create_report(
        self,
        report_data: ReportCreate,
        current_user: User,
        analysis: AnalysisResult,
    ) -> Report:

        # ai_service = AIService()

        # analysis = ai_service.analyze(
        #     report_data.selected_text
        # )

        report = Report(
            user_id=current_user.id,
            case_id=self._generate_case_id(),

            platform=report_data.platform,
            display_name=report_data.display_name,
            username=report_data.username,
            profile_url=str(report_data.profile_url) if report_data.profile_url else None,
            post_url=str(report_data.post_url) if report_data.post_url else None,
            selected_text=report_data.selected_text,

            classification=analysis.classification,
            ai_explanation=analysis.explanation,
            severity=analysis.severity,
            confidence=analysis.confidence,
            language=analysis.language,
            status=ReportStatus.ANALYZED,
        )

        return self.repository.create(report)

    def get_my_reports(self, current_user: User):
        return self.repository.get_by_user(current_user.id)

    def get_report(
        self,
        report_id,
        current_user: User,
    ):

        report = self.repository.get_by_id(report_id)

        if report is None:
            return None

        if report.user_id != current_user.id:
            return None

        return report

    def delete_report(
        self,
        report_id,
        current_user: User,
    ) -> bool:

        report = self.get_report(report_id, current_user)

        if report is None:
            return False

        self.repository.delete(report)

        return True