from pathlib import Path
from datetime import datetime

from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet


class PDFGenerator:

    STORAGE_DIR = Path("storage/pdfs")

    @classmethod
    def generate(cls, report, evidence_hash: str):

        cls.STORAGE_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = f"{report.case_id}.pdf"

        filepath = cls.STORAGE_DIR / filename

        styles = getSampleStyleSheet()

        document = SimpleDocTemplate(str(filepath))

        elements = []

        elements.append(
            Paragraph(
                "<b>ARAN Evidence Report</b>",
                styles["Title"],
            )
        )

        elements.append(Spacer(1, 0.3 * inch))

        elements.append(
            Paragraph(f"<b>Case ID:</b> {report.case_id}", styles["BodyText"])
        )

        elements.append(
            Paragraph(f"<b>Platform:</b> {report.platform.value}", styles["BodyText"])
        )

        elements.append(
            Paragraph(f"<b>Username:</b> @{report.username}", styles["BodyText"])
        )

        elements.append(
            Paragraph(
                f"<b>Display Name:</b> {report.display_name}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Reported Text:</b><br/>{report.selected_text}",
                styles["BodyText"],
            )
        )

        elements.append(Spacer(1, 0.2 * inch))

        elements.append(
            Paragraph(
                "<b>AI Analysis</b>",
                styles["Heading2"],
            )
        )

        elements.append(
            Paragraph(
                f"Classification: {report.classification}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"Severity: {report.severity.value}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"Confidence: {report.confidence}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"Language: {report.language}",
                styles["BodyText"],
            )
        )

        elements.append(Spacer(1, 0.2 * inch))

        elements.append(
            Paragraph(
                "<b>Evidence Integrity</b>",
                styles["Heading2"],
            )
        )

        elements.append(
            Paragraph(
                f"SHA-256: {evidence_hash}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"Generated: {datetime.utcnow()} UTC",
                styles["BodyText"],
            )
        )

        document.build(elements)

        return filename, str(filepath)