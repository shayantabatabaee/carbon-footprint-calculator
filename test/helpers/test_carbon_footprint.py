import asyncio
import os

import pytest
from pubsub import pub

from carbon_footprint_calculator.assets.constants import COMPANY_PDF_PATH, COMPANY_PLOT_PATH, FULL_PLOT_PATH, \
    FULL_PDF_PATH
from carbon_footprint_calculator.helpers.carbon_footprint import CarbonFootprint
from carbon_footprint_calculator.helpers.company_repository import CompanyRepository
from carbon_footprint_calculator.models.business_travel import BusinessTravel
from carbon_footprint_calculator.models.energy_usage import EnergyUsage
from carbon_footprint_calculator.models.waste import Waste


class TestCarbonFootprint:

    @staticmethod
    @pytest.mark.integration
    def test_generate_full_report():
        repository: CompanyRepository = CompanyRepository.get_instance()
        repository.clear()
        repository.add('Company 1', 1, 1, 1, 3)
        repository.add('Company 2', 2, 2, 2, 6)

        event = asyncio.Event()

        def on_report_ready(report_type: str):
            event.set()

        pub.subscribe(on_report_ready, CarbonFootprint.CHANNEL)
        CarbonFootprint.generate_full_report()

        assert os.path.isfile(FULL_PLOT_PATH) == True
        assert os.path.isfile(FULL_PDF_PATH) == True

    @staticmethod
    @pytest.mark.integration
    def test_generate_company_report():
        energy_usage_dto = EnergyUsage(monthly_electricity_bill=1, monthly_natural_gas_bill=1, monthly_fuel_bill=1)
        waste_dto = Waste(total_waste_generated_monthly=1, recycling_percentage=1)
        business_travel_dto = BusinessTravel(total_kilometers_traveled_yearly=1, average_fuel_efficiency=1)

        event = asyncio.Event()

        def on_report_ready(report_type: str):
            event.set()

        pub.subscribe(on_report_ready, CarbonFootprint.CHANNEL)
        CarbonFootprint.generate_company_report('Test', energy_usage_dto, waste_dto, business_travel_dto)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(asyncio.wait_for(event.wait(), timeout=20))
        loop.close()

        assert os.path.isfile(COMPANY_PLOT_PATH) == True
        assert os.path.isfile(COMPANY_PDF_PATH) == True
