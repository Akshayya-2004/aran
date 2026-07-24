from fastapi import FastAPI

app = FastAPI(
    title="ARAN API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "ARAN Backend Running"
    }