from fastapi import FastAPI, HTTPException
from api.schemas import ForecastRequest, ForecastResponse
from models.load_model import load_model

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
    model = load_model(request.store_id, request.product_id)
    
    if model is None:
        raise HTTPException(
            status_code=404,
            detail=f"Model not found for {request.store_id}-{request.product_id}"
        )
    
    future = model.make_future_dataframe(periods=request.days)
    forecast_df = model.predict(future).tail(request.days)
    
    forecasts = [
        {"date": str(row.ds.date()), "forecast": float(row.yhat)}
        for _, row in forecast_df.iterrows()
    ]
    
    return ForecastResponse(
        store_id=request.store_id,
        product_id=request.product_id,
        horizon_days=request.days,
        forecasts=forecasts,
    )
