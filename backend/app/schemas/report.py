from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, HttpUrl

from app.enums import Platform, Severity, ReportStatus


class ReportCreate(BaseModel):

    platform: Platform

    display_name: str

    username: str

    profile_url: HttpUrl | None = None

    post_url: HttpUrl | None = None

    selected_text: str


class ReportResponse(BaseModel):

    id: UUID

    case_id: str

    platform: Platform

    display_name: str

    username: str

    profile_url: str | None

    post_url: str | None

    selected_text: str

    classification: str

    severity: Severity

    confidence: float

    language: str

    status: ReportStatus

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ReportListResponse(BaseModel):

    id: UUID

    case_id: str

    platform: Platform

    username: str

    severity: Severity

    status: ReportStatus

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)