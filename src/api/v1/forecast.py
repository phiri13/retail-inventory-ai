from fastapi import APIRouter, HTTPException
from api.schemas import ForecastRequest, ForecastResponse
from models.load_model import load_model

router = APIRouter(tags=["forecast"])

@router.post("/forecast", response_model=ForecastResponse)
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

