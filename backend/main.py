from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="LegalEase API",
    description="AI-Powered Legal Document Generator",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "LegalEase API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


app.include_router(router)