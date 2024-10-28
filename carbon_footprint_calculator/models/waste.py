from pydantic import BaseModel, Field


class Waste(BaseModel):
    total_waste_generated_monthly: float = Field(..., ge=0)
    recycling_percentage: float = Field(..., ge=0, le=100)
