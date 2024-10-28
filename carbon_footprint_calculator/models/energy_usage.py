from pydantic import BaseModel, Field


class EnergyUsage(BaseModel):
    monthly_electricity_bill: float = Field(..., ge=0)
    monthly_natural_gas_bill: float = Field(..., ge=0)
    monthly_fuel_bill: float = Field(..., ge=0)
