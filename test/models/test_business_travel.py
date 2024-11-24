import pytest
from pydantic import ValidationError

from carbon_footprint_calculator.models.business_travel import BusinessTravel


class TestBusinessTravel:

    @staticmethod
    @pytest.mark.unit
    @pytest.mark.parametrize('total_kilometers_traveled_yearly, average_fuel_efficiency, expected_error',
                             [(-2, 5, ValidationError),
                              (5, -2, ValidationError)
                              ],
                             ids=['Negative Total Kilometers', 'Negative Fuel Efficiency'])
    def test_business_travel_validation(total_kilometers_traveled_yearly: float,
                                        average_fuel_efficiency: float,
                                        expected_error):
        with pytest.raises(expected_error):
            assert BusinessTravel(total_kilometers_traveled_yearly=total_kilometers_traveled_yearly,
                                  average_fuel_efficiency=average_fuel_efficiency)
