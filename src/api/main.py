from fastapi import FastAPI, HTTPException
from datetime import timedelta
import pandas as pd

from src.models.load_model import load_models

app = FastAPI(title="RetailAI-ZA Forecast API")

models = load_models()

@app.post("/forecast")
def forecast(store_id: str, product_id: str, days: int = 30):
    key = f"{store_id}_{product_id}"

    if key not in models:
        raise HTTPException(status_code=404, detail="Model not found")

    model = models[key]
    last_date = model.history["ds"].max()
    future = pd.DataFrame({
        "ds": [last_date + timedelta(days=i+1) for i in range(days)]
    })

    forecast = model.predict(future)

    return {
        "store_id": store_id,
        "product_id": product_id,
        "forecast": [
            {"date": row.ds.date().isoformat(), "units": int(row.yhat)}
            for _, row in forecast.iterrows()
        ]
    }
