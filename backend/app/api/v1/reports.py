from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models import User
from app.repositories import ReportRepository
from app.schemas import (
    ReportCreate,
    ReportResponse,
    ReportListResponse,
)
from app.repositories import (
    ReportRepository,
    EvidenceRepository,
)

from app.services import (
    ReportService,
    ReportWorkflowService,
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.post(
    "",
    response_model=ReportResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_report(
    report_data: ReportCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    workflow = ReportWorkflowService(
        report_repository=ReportRepository(db),
        evidence_repository=EvidenceRepository(db),
    )

    return workflow.create_report(
        report_data,
        current_user,
    )

@router.get(
    "",
    response_model=list[ReportListResponse],
)
def get_my_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ReportRepository(db)
    service = ReportService(repository)

    return service.get_my_reports(current_user)


@router.get(
    "/{report_id}",
    response_model=ReportResponse,
)
def get_report(
    report_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ReportRepository(db)
    service = ReportService(repository)

    report = service.get_report(report_id, current_user)

    if report is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found",
        )

    return report


@router.delete(
    "/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_report(
    report_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ReportRepository(db)
    service = ReportService(repository)

    deleted = service.delete_report(
        report_id,
        current_user,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found",
        )