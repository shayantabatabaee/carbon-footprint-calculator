import logging

import numpy as np
from pubsub import pub

from carbon_footprint_calculator.assets.constants import COMPANY_PLOT_PATH, COMPANY_PDF_PATH, FULL_PLOT_PATH, \
    FULL_PDF_PATH
from carbon_footprint_calculator.assets.strings import labels, full_report
from carbon_footprint_calculator.helpers.company_repository import CompanyRepository
from carbon_footprint_calculator.helpers.llm_interpreter import LLMInterpreter
from carbon_footprint_calculator.helpers.pdf_generator import PDFGenerator
from carbon_footprint_calculator.helpers.plot import Plot
from carbon_footprint_calculator.models.business_travel import BusinessTravel
from carbon_footprint_calculator.models.energy_usage import EnergyUsage
from carbon_footprint_calculator.models.llm_result import LLMResult
from carbon_footprint_calculator.models.waste import Waste
from carbon_footprint_calculator.utils.calculator import Calculator


class CarbonFootprint:
    CHANNEL = "REPORT_READY_CHANNEL"

    @staticmethod
    def generate_full_report():
        repository: CompanyRepository = CompanyRepository.get_instance()

        if len(repository.get_all()) < 2:
            pub.sendMessage(CarbonFootprint.CHANNEL, report_type=None)
            raise ValueError(labels['EMPTY_COMPANY_TITLE'],
                             labels['EMPTY_COMPANY_TEXT'] + f', count: {len(repository.get_all())}')

        content = full_report
        sorted_company_names = sorted(repository.get_all(),
                                      key=lambda name: repository.get_all()[name]['total_usage'],
                                      reverse=True)
        weights_count = {
            'Energy Usage': np.array([]),
            'Generated Waste': np.array([]),
            'Business Travel Usage': np.array([])
        }

        table = '<table style="border: 1px solid black;text-align: center;height: 30px;"><tr><th>Company Name</th><th>Energy Usage</th><th>Generated Waste</th><th>Business Travel Usage</th><th>Total Usage</th></tr>'

        for company in sorted_company_names:
            weights_count['Energy Usage'] = np.append(weights_count['Energy Usage'],
                                                      repository.get(company)['energy_usage'])
            weights_count['Generated Waste'] = np.append(weights_count['Generated Waste'],
                                                         repository.get(company)['generated_waste'])
            weights_count['Business Travel Usage'] = np.append(weights_count['Business Travel Usage'],
                                                               repository.get(company)['business_travel_usage'])
            table += (f'<tr>'
                      f'<td>{company}</td>'
                      f'<td>{repository.get(company)['energy_usage']}</td>'
                      f'<td>{repository.get(company)['generated_waste']}</td>'
                      f'<td>{repository.get(company)['business_travel_usage']}</td>'
                      f'<td>{repository.get(company)['total_usage']}</td>'
                      f'</tr>')

        table += '</table>'

        Plot.draw_bar_chart(sorted_company_names, weights_count, FULL_PLOT_PATH)

        content = content.format(sorted_company_names[0], table, FULL_PLOT_PATH)
        PDFGenerator.generate(content, FULL_PDF_PATH)
        pub.sendMessage(CarbonFootprint.CHANNEL, report_type='FULL')

    @staticmethod
    def generate_company_report(company_name: str,
                                energy_usage_dto: EnergyUsage,
                                waste_dto: Waste,
                                business_travel_dto: BusinessTravel):
        repository: CompanyRepository = CompanyRepository.get_instance()

        energy_usage = Calculator.calculate_energy_usage(energy_usage_dto)
        generated_waste = Calculator.calculate_waste(waste_dto)
        business_travel_usage = Calculator.calculate_business_travel(business_travel_dto)
        total_usage = energy_usage + generated_waste + business_travel_usage

        logging.info(f"Carbon foot print calculated successfully, "
                     f"summary: Energy: {energy_usage}, Waste: {generated_waste}, Business Travel: {business_travel_usage}")

        plot_labels = labels['ENERGY_USAGE_TITLE'], labels['WASTE_TITLE'], labels['BUSINESS_TRAVEL_TITLE']
        colors = ['#dedce5', '#dfe6ee', '#dbc3cd']

        repository.add(company_name, energy_usage, generated_waste, business_travel_usage, total_usage)
        Plot.draw_pie_chart(plot_labels, [energy_usage, generated_waste, business_travel_usage], colors,
                            COMPANY_PLOT_PATH)
        pub.subscribe(CarbonFootprint.__llm_report_ready, LLMInterpreter.CHANNEL)
        LLMInterpreter.report(company_name, energy_usage, generated_waste, business_travel_usage, total_usage)

    @staticmethod
    def __llm_report_ready(llm_result: LLMResult):
        if not llm_result.is_successful:
            pub.sendMessage(CarbonFootprint.CHANNEL, report_type=None)
            raise llm_result.error
        content = llm_result.result['choices'][0]['message']['content']
        content += '\n\n'
        content += '**Plot**'
        content += '\n\n'
        content += 'The plot for carbon footprint is as follows:\n'
        content += f'![Pie Chart]({COMPANY_PLOT_PATH})'
        PDFGenerator.generate(content, COMPANY_PDF_PATH)
        pub.sendMessage(CarbonFootprint.CHANNEL, report_type='COMPANY')
