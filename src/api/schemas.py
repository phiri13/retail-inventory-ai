from pydantic import BaseModel, Field
from typing import List


class ForecastRequest(BaseModel):
    store_id: str = Field(..., example="JHB_01")
    product_id: str = Field(..., example="BREAD")
    days: int = Field(30, ge=1, le=180)


class ForecastPoint(BaseModel):
    date: str
    forecast: float


class ForecastResponse(BaseModel):
    store_id: str
    product_id: str
    horizon_days: int
    forecasts: List[ForecastPoint]
