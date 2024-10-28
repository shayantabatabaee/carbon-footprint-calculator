from pydantic import BaseModel, Field


class BusinessTravel(BaseModel):
    total_kilometers_traveled_yearly: float = Field(..., ge=0)
    average_fuel_efficiency: float = Field(..., ge=0)
