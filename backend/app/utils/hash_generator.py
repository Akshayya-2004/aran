import hashlib
import json


class HashGenerator:

    @staticmethod
    def generate(report) -> str:
        """
        Generate a SHA-256 hash based on the report data.
        """

        report_data = {
            "case_id": report.case_id,
            "platform": report.platform.value,
            "display_name": report.display_name,
            "username": report.username,
            "profile_url": report.profile_url,
            "post_url": report.post_url,
            "selected_text": report.selected_text,
            "classification": report.classification,
            "severity": report.severity.value,
            "confidence": report.confidence,
            "language": report.language,
            "status": report.status.value,
        }

        # Convert dictionary to a deterministic JSON string
        serialized = json.dumps(
            report_data,
            sort_keys=True,
            ensure_ascii=False,
        )

        # Generate SHA-256 hash
        return hashlib.sha256(
            serialized.encode("utf-8")
        ).hexdigest()