print("Step 1")

from app.services.ai_service import AIService

print("Step 2")

service = AIService()

print("Step 3")

analysis = service.analyze(
    "You are an idiot. Nobody likes you."
)

print("Step 4")

print(type(analysis))
print(analysis)