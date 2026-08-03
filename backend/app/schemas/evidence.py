from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class EvidenceResponse(BaseModel):
    id: UUID
    report_id: UUID
    generated: bool
    file_hash: str
    generated_at: datetime | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PDFResponse(BaseModel):
    id: UUID
    report_id: UUID
    file_name: str
    file_path: str
    generated_at: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)