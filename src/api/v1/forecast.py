from fastapi import APIRouter, HTTPException
from api.schemas import ForecastRequest, ForecastResponse
from models.load_model import load_model

router = APIRouter()

@router.post("/forecast")
def forecast(request: ForecastRequest):
    model = load_model(request.store_id, request.product_id)

    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")

    preds = model.predict(request.days)

    return {
        "store_id": request.store_id,
        "product_id": request.product_id,
        "horizon_days": request.days,
        "forecasts": preds
    }

from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

limiter = Limiter(key_func=get_remote_address)

@router.post("/forecast")
@limiter.limit("5/minute")
def forecast(request: ForecastRequest, request_obj: Request):
    ...
