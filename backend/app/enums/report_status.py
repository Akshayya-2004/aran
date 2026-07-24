from enum import Enum


class ReportStatus(str, Enum):
    ANALYZING = "ANALYZING"
    ANALYZED = "ANALYZED"
    PDF_READY = "PDF_READY"
    FAILED = "FAILED"