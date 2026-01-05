from fastapi import FastAPI
from api.v1.forecast import router as forecast_router
from api.v1.health import router as health_router

app = FastAPI(title="RetailAI-ZA Forecast API")

app.include_router(health_router)
app.include_router(forecast_router)

