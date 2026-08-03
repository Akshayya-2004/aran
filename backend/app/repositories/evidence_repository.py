from uuid import UUID

from sqlalchemy.orm import Session

from app.models import Evidence, PDF


class EvidenceRepository:

    def __init__(self, db: Session):
        self.db = db

    # ---------- Evidence ----------

    def create_evidence(self, evidence: Evidence) -> Evidence:
        self.db.add(evidence)
        self.db.commit()
        self.db.refresh(evidence)
        return evidence

    def get_evidence_by_report_id(
        self,
        report_id: UUID,
    ) -> Evidence | None:
        return (
            self.db.query(Evidence)
            .filter(Evidence.report_id == report_id)
            .first()
        )

    # ---------- PDF ----------

    def create_pdf(self, pdf: PDF) -> PDF:
        self.db.add(pdf)
        self.db.commit()
        self.db.refresh(pdf)
        return pdf

    def get_pdf_by_report_id(
        self,
        report_id: UUID,
    ) -> PDF | None:
        return (
            self.db.query(PDF)
            .filter(PDF.report_id == report_id)
            .first()
        )