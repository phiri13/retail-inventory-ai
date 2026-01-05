from fastapi import FastAPI

app = FastAPI(
    title="RetailAI-ZA Forecast API",
    version="0.1.0"
)

@app.get("/health", tags=["system"])
def health_check():
    return {
        "status": "ok",
        "service": "forecast-api",
        "model_backend": "prophet",
        "environment": "local"
    }

