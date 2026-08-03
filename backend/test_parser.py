from app.ai.response_parser import parse_response

response = """
{
    "classification": "Harassment",
    "severity": "HIGH",
    "confidence": 0.95,
    "language": "English",
    "explanation": "The post contains abusive language."
}
"""

analysis = parse_response(response)

print(type(analysis))
print(analysis)
print(analysis.classification)
print(analysis.severity)
print(analysis.confidence)
print(analysis.language)
print(analysis.explanation)