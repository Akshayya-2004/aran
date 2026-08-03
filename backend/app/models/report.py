import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey,
    func,
    Enum as SQLEnum
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base
from app.enums import Platform, Severity, ReportStatus


class Report(Base):

    __tablename__ = "reports"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    case_id = Column(
        String(30),
        unique=True,
        nullable=False
    )

    platform = Column(
        SQLEnum(Platform),
        nullable=False,
        default=Platform.TWITTER,
        index=True
    )

    display_name = Column(
        String(100),
        nullable=False
    )

    username = Column(
        String(100),
        nullable=False
    )

    profile_url = Column(Text)

    post_url = Column(Text)

    selected_text = Column(
        Text,
        nullable=False
    )

    classification = Column(
        String(100),
        nullable=False
    )

    severity = Column(
        SQLEnum(Severity),
        nullable=False,
        index=True
    )

    confidence = Column(
        Float,
        nullable=False
    )

    language = Column(
        String(20),
        nullable=False
    )

    status = Column(
        SQLEnum(ReportStatus),
        nullable=False,
        default=ReportStatus.ANALYZING,
        index=True
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="reports"
    )

    evidence = relationship(
        "Evidence",
        back_populates="report",
        uselist=False,
        cascade="all, delete-orphan"
    )

    pdf = relationship(
        "PDF",
        back_populates="report",
        uselist=False,
        cascade="all, delete-orphan"
    )