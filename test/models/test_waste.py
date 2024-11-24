import pytest
from pydantic import ValidationError

from carbon_footprint_calculator.models.waste import Waste


class TestWaste:

    @staticmethod
    @pytest.mark.unit
    @pytest.mark.parametrize('total_waste_generated_monthly, recycling_percentage, expected_error',
                             [(-2, 5, ValidationError),
                              (5, -2, ValidationError),
                              (5, 110, ValidationError)],
                             ids=['Negative Waste',
                                  'Negative Recycling Percentage',
                                  'Greater Than 100 Recycling Percentage'])
    def test_business_travel_validation(total_waste_generated_monthly: float,
                                        recycling_percentage: float,
                                        expected_error):
        with pytest.raises(expected_error):
            assert Waste(total_waste_generated_monthly=total_waste_generated_monthly,
                         recycling_percentage=recycling_percentage)
