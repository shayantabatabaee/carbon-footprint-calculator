import pytest

from carbon_footprint_calculator.models.business_travel import BusinessTravel
from carbon_footprint_calculator.models.energy_usage import EnergyUsage
from carbon_footprint_calculator.models.waste import Waste
from carbon_footprint_calculator.utils.calculator import Calculator


class TestCalculator:

    @staticmethod
    @pytest.mark.unit
    @pytest.mark.parametrize('energy_usage , expected',
                             [(EnergyUsage(monthly_electricity_bill=1,
                                           monthly_natural_gas_bill=1,
                                           monthly_fuel_bill=1), 27.9096)],
                             ids=['Calculate Energy Usage'])
    def test_calculate_energy_usage(energy_usage: EnergyUsage, expected: float):
        energy_usage = Calculator.calculate_energy_usage(energy_usage)
        assert round(energy_usage, 4) == expected

    @staticmethod
    @pytest.mark.unit
    @pytest.mark.parametrize('waste , expected',
                             [(Waste(total_waste_generated_monthly=1,
                                     recycling_percentage=1), 6.72)],
                             ids=['Calculate Waste'])
    def test_calculate_waste(waste: Waste, expected: float):
        waste_usage = Calculator.calculate_waste(waste)
        assert round(waste_usage, 2) == expected

    @staticmethod
    @pytest.mark.unit
    @pytest.mark.parametrize('business_travel , expected',
                             [(BusinessTravel(total_kilometers_traveled_yearly=1,
                                              average_fuel_efficiency=1), 2.31)],
                             ids=['Calculate Business Travel Usage'])
    def test_calculate_business_travel(business_travel: BusinessTravel, expected: float):
        business_travel_usage = Calculator.calculate_business_travel(business_travel)
        assert round(business_travel_usage, 2) == expected
