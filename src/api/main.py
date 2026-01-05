from fastapi import FastAPI
from src.api.schemas import ForecastRequest, ForecastResponse

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
        "environment": "local",
    }


@app.post("/forecast", response_model=ForecastResponse)
def forecast(request: ForecastRequest):
    # TEMP placeholder — real model wiring comes later
    return {
        "store_id": request.store_id,
        "product_id": request.product_id,
        "horizon_days": request.days,
        "forecasts": [
            {"date": "2025-01-01", "forecast": 123.4}
        ],
    }

