import logging

from carbon_footprint_calculator.assets.strings import labels
from carbon_footprint_calculator.helpers.plot import Plot
from carbon_footprint_calculator.models.business_travel import BusinessTravel
from carbon_footprint_calculator.models.energy_usage import EnergyUsage
from carbon_footprint_calculator.models.waste import Waste
from carbon_footprint_calculator.utils.calculator import Calculator


class CarbonFootprint:

    @staticmethod
    def generate_report(energy_usage_dto: EnergyUsage, waste_dto: Waste, business_travel_dto: BusinessTravel):
        energy_usage = Calculator.calculate_energy_usage(energy_usage_dto)
        waste_usage = Calculator.calculate_waste(waste_dto)
        business_travel_usage = Calculator.calculate_business_travel(business_travel_dto)

        logging.info(f"Carbon foot print calculated successfully, "
                     f"summary: Energy: {energy_usage}, Waste: {waste_usage}, Business Travel: {business_travel_usage}")

        plot_labels = labels['ENERGY_USAGE_TITLE'], labels['WASTE_TITLE'], labels['BUSINESS_TRAVEL_TITLE']
        colors = ['#dedce5', '#dfe6ee', '#dbc3cd']
        Plot.draw(plot_labels, [energy_usage, waste_usage, business_travel_usage], colors)
