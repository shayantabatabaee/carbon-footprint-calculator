import pytest
from pydantic import ValidationError

from carbon_footprint_calculator.models.energy_usage import EnergyUsage


class TestEnergyUsage:

    @staticmethod
    @pytest.mark.unit
    @pytest.mark.parametrize('monthly_electricity_bill, monthly_natural_gas_bill, monthly_fuel_bill, expected_error',
                             [(-2, 5, 5, ValidationError),
                              (5, -2, 5, ValidationError),
                              (5, 5, -2, ValidationError)
                              ],
                             ids=['Negative Electricity Bill', 'Negative Natural Gas Bill', 'Negative Fuel Bill'])
    def test_business_travel_validation(monthly_electricity_bill: float,
                                        monthly_natural_gas_bill: float,
                                        monthly_fuel_bill: float,
                                        expected_error):
        with pytest.raises(expected_error):
            assert EnergyUsage(monthly_electricity_bill=monthly_electricity_bill,
                               monthly_natural_gas_bill=monthly_natural_gas_bill,
                               monthly_fuel_bill=monthly_fuel_bill
                               )
