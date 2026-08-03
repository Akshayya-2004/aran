from uuid import UUID

from sqlalchemy.orm import Session

from app.models.report import Report


class ReportRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, report: Report) -> Report:
        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)
        return report

    def get_by_id(self, report_id: UUID) -> Report | None:
        return (
            self.db.query(Report)
            .filter(Report.id == report_id)
            .first()
        )

    def get_by_case_id(self, case_id: str) -> Report | None:
        return (
            self.db.query(Report)
            .filter(Report.case_id == case_id)
            .first()
        )

    def get_by_user(self, user_id: UUID) -> list[Report]:
        return (
            self.db.query(Report)
            .filter(Report.user_id == user_id)
            .order_by(Report.created_at.desc())
            .all()
        )

    def delete(self, report: Report) -> None:
        self.db.delete(report)
        self.db.commit()