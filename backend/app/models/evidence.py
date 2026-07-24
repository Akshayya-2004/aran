import uuid

from sqlalchemy import Column, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class Evidence(Base):

    __tablename__ = "evidence"

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

    generated = Column(
        Boolean,
        nullable=False,
        default=False
    )

    hash = Column(
        String(64),
        nullable=False,
        unique=True
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
        back_populates="evidence"
    )