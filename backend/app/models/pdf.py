import uuid

from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class PDF(Base):

    __tablename__ = "pdfs"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    report_id = Column(
        UUID(as_uuid=True),
        ForeignKey("reports.id"),
        unique=True,
        nullable=False
    )

    file_name = Column(
        String(255),
        nullable=False
    )

    file_path = Column(
        Text,
        nullable=False
    )

    generated_at = Column(
        DateTime(timezone=True),
        nullable=False
    )

    # created_at = Column(
    #     DateTime(timezone=True),
    #     server_default=func.now(),
    #     nullable=False
    # )

    report = relationship(
        "Report",
        back_populates="pdf"
    )