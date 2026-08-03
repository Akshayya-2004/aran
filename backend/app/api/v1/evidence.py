from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models import User
from app.repositories import (
    ReportRepository,
    EvidenceRepository,
)
from app.services import (
    ReportService,
    EvidenceService,
)
from app.schemas import EvidenceResponse

router = APIRouter(
    prefix="/reports",
    tags=["Evidence"],
)


@router.get(
    "/{report_id}/evidence",
    response_model=EvidenceResponse,
)
def get_evidence(
    report_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    report_service = ReportService(
        ReportRepository(db)
    )

    report = report_service.get_report(
        report_id,
        current_user,
    )

    if report is None:
        raise HTTPException(
            404,
            "Report not found",
        )

    evidence_service = EvidenceService(
        EvidenceRepository(db)
    )

    evidence = evidence_service.get_evidence(report.id)

    if evidence is None:
        raise HTTPException(
            404,
            "Evidence not found",
        )

    return evidence


@router.get("/{report_id}/pdf")
def download_pdf(
    report_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    report_service = ReportService(
        ReportRepository(db)
    )

    report = report_service.get_report(
        report_id,
        current_user,
    )

    if report is None:
        raise HTTPException(
            404,
            "Report not found",
        )

    evidence_service = EvidenceService(
        EvidenceRepository(db)
    )

    pdf = evidence_service.get_pdf(report.id)

    if pdf is None:
        raise HTTPException(
            404,
            "PDF not found",
        )

    return FileResponse(
        path=pdf.file_path,
        filename=pdf.file_name,
        media_type="application/pdf",
    )