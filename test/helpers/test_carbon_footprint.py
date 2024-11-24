import asyncio
import os

import pytest
from pubsub import pub

from carbon_footprint_calculator.assets.constants import PDF_PATH, PLOT_PATH
from carbon_footprint_calculator.helpers.carbon_footprint import CarbonFootprint
from carbon_footprint_calculator.models.business_travel import BusinessTravel
from carbon_footprint_calculator.models.energy_usage import EnergyUsage
from carbon_footprint_calculator.models.waste import Waste


class TestCarbonFootprint:

    @staticmethod
    @pytest.mark.integration
    def test_generate_report():
        energy_usage_dto = EnergyUsage(monthly_electricity_bill=1, monthly_natural_gas_bill=1, monthly_fuel_bill=1)
        waste_dto = Waste(total_waste_generated_monthly=1, recycling_percentage=1)
        business_travel_dto = BusinessTravel(total_kilometers_traveled_yearly=1, average_fuel_efficiency=1)

        event = asyncio.Event()

        def on_report_ready():
            event.set()

        pub.subscribe(on_report_ready, CarbonFootprint.CHANNEL)
        CarbonFootprint.generate_report(energy_usage_dto, waste_dto, business_travel_dto)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(asyncio.wait_for(event.wait(), timeout=20))
        loop.close()

        assert os.path.isfile(PLOT_PATH) == True
        assert os.path.isfile(PDF_PATH) == True
