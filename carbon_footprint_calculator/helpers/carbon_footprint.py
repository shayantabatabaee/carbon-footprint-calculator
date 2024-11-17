import logging

from carbon_footprint_calculator.assets.constants import PLOT_PATH
from carbon_footprint_calculator.assets.strings import labels
from carbon_footprint_calculator.helpers.llm_interpreter import LLMInterpreter
from carbon_footprint_calculator.helpers.pdf_generator import PDFGenerator
from carbon_footprint_calculator.helpers.plot import Plot
from carbon_footprint_calculator.models.business_travel import BusinessTravel
from carbon_footprint_calculator.models.energy_usage import EnergyUsage
from carbon_footprint_calculator.models.llm_result import LLMResult
from carbon_footprint_calculator.models.waste import Waste
from carbon_footprint_calculator.utils.calculator import Calculator


class CarbonFootprint:

    @staticmethod
    def generate_report(energy_usage_dto: EnergyUsage, waste_dto: Waste, business_travel_dto: BusinessTravel):
        energy_usage = Calculator.calculate_energy_usage(energy_usage_dto)
        generated_waste = Calculator.calculate_waste(waste_dto)
        business_travel_usage = Calculator.calculate_business_travel(business_travel_dto)

        logging.info(f"Carbon foot print calculated successfully, "
                     f"summary: Energy: {energy_usage}, Waste: {generated_waste}, Business Travel: {business_travel_usage}")

        plot_labels = labels['ENERGY_USAGE_TITLE'], labels['WASTE_TITLE'], labels['BUSINESS_TRAVEL_TITLE']
        colors = ['#dedce5', '#dfe6ee', '#dbc3cd']
        Plot.draw(plot_labels, [energy_usage, generated_waste, business_travel_usage], colors)
        LLMInterpreter.report(energy_usage, generated_waste, business_travel_usage,
                              callback=CarbonFootprint.__llm_report_ready)

    @staticmethod
    def __llm_report_ready(llm_result: LLMResult):
        if not llm_result.is_successful:
            raise llm_result.error
        content = llm_result.result['choices'][0]['message']['content']
        content += '\n\n'
        content += '**Plot**'
        content += '\n\n'
        content += 'The plot for carbon footprint is as follows:\n'
        content += f'![Pie Chart]({PLOT_PATH})'
        PDFGenerator.generate(content)
