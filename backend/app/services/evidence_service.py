from datetime import datetime, timezone

from app.models import Evidence, PDF, Report
from app.repositories import EvidenceRepository
from app.utils.hash_generator import HashGenerator
from app.utils.pdf_generator import PDFGenerator

class EvidenceService:

    def __init__(self, repository: EvidenceRepository):
        self.repository = repository

    def generate_evidence(self, report: Report) -> tuple[Evidence, PDF]:

        # Generate SHA-256 hash
        file_hash = HashGenerator.generate(report)

        # Generate PDF
        file_name, file_path = PDFGenerator.generate(
            report,
            file_hash,
        )

        now = datetime.now(timezone.utc)

        evidence = Evidence(
            report_id=report.id,
            generated=True,
            file_hash=file_hash,
            generated_at=now,
        )

        pdf = PDF(
            report_id=report.id,
            file_name=file_name,
            file_path=file_path,
            generated_at=now,
        )

        evidence = self.repository.create_evidence(evidence)
        pdf = self.repository.create_pdf(pdf)

        return evidence, pdf

    def get_evidence(self, report_id):
        return self.repository.get_evidence_by_report_id(report_id)

    def get_pdf(self, report_id):
        return self.repository.get_pdf_by_report_id(report_id)