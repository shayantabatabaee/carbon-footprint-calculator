from carbon_footprint_calculator.models.business_travel import BusinessTravel
from carbon_footprint_calculator.models.energy_usage import EnergyUsage
from carbon_footprint_calculator.models.waste import Waste


class Calculator:

    @staticmethod
    def calculate_energy_usage(energy_usage: EnergyUsage) -> float:
        return (energy_usage.monthly_electricity_bill * 12 * 0.0005) + \
            (energy_usage.monthly_natural_gas_bill * 12 * 0.0053) + \
            (energy_usage.monthly_fuel_bill * 12 * 2.32)

    @staticmethod
    def calculate_waste(waste: Waste):
        return waste.total_waste_generated_monthly * 12 * (0.57 - waste.recycling_percentage)

    @staticmethod
    def calculate_business_travel(business_travel: BusinessTravel) -> float:
        return (business_travel.total_kilometers_traveled_yearly / business_travel.average_fuel_efficiency) * 2.31
