from app.core.config import settings

print(settings.DATABASE_URL)
print(settings.GEMINI_MODEL)
print(settings.GEMINI_API_KEY[:10] + "...")