from fastapi import APIRouter, HTTPException
from src.models.load_model import (
    load_model,
    ModelNotFoundError,
    InvalidModelMetadataError,
)

router = APIRouter(prefix="/forecast", tags=["forecast"])


@router.post("")
def forecast(store_id: str, product_id: str):
    try:
        model, metadata = load_model(store_id, product_id)
    except ModelNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except InvalidModelMetadataError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Model loading failed")

    # Placeholder prediction logic
    horizon = metadata["horizon_days"]
    return {
        "store_id": store_id,
        "product_id": product_id,
        "horizon_days": horizon,
        "forecasts": [
            {"day": i + 1, "forecast": 0.0} for i in range(horizon)
        ],
    }

