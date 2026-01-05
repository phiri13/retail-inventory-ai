from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from api.v1.health import router as health_router
from api.v1.forecast import router as forecast_router

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="RetailAI-ZA Forecast API",
    version="1.0.0"
)

app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"}
    )

# 🔑 VERSIONED ROUTING
app.include_router(health_router, prefix="/v1")
app.include_router(forecast_router, prefix="/v1")

