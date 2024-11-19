import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFrame, QLabel, QHBoxLayout, QLineEdit, QStackedLayout
from pubsub import pub

from carbon_footprint_calculator.assets.strings import labels
from carbon_footprint_calculator.helpers.carbon_footprint import CarbonFootprint
from carbon_footprint_calculator.helpers.llm_interpreter import LLMInterpreter
from carbon_footprint_calculator.models.business_travel import BusinessTravel
from carbon_footprint_calculator.models.energy_usage import EnergyUsage
from carbon_footprint_calculator.models.waste import Waste
from carbon_footprint_calculator.ui.loading import Loading
from carbon_footprint_calculator.ui.push_button import PushButton
from carbon_footprint_calculator.ui.widget import Widget


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # Input Variables
        self.energy_first_input: QLineEdit = None
        self.energy_second_input: QLineEdit = None
        self.energy_third_input: QLineEdit = None
        self.waste_first_input: QLineEdit = None
        self.waste_second_input: QLineEdit = None
        self.travel_first_input: QLineEdit = None
        self.travel_second_input: QLineEdit = None

        self.setFixedSize(550, 650)
        self.setWindowTitle(labels['WINDOW_TITLE'])
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.loading_widget = Loading()

        self.main_layout = QStackedLayout()

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        image_path = os.path.join(os.getcwd(), 'assets', 'logo.png')
        logo_label = QLabel()

        logo_image = QPixmap(image_path)
        logo_label.setPixmap(logo_image)
        content_layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        # First Widget
        widget_1 = Widget(labels['ENERGY_USAGE_TITLE'], [labels['ENERGY_USAGE_QUESTION_1'],
                                                         labels['ENERGY_USAGE_QUESTION_2'],
                                                         labels['ENERGY_USAGE_QUESTION_3']])
        self.energy_first_input = widget_1.question_inputs[0]
        self.energy_second_input = widget_1.question_inputs[1]
        self.energy_third_input = widget_1.question_inputs[2]
        horizontal_line_1 = QFrame()
        horizontal_line_1.setFrameShape(QFrame.Shape.HLine)
        horizontal_line_1.setFrameShadow(QFrame.Shadow.Sunken)
        horizontal_line_1.setFixedWidth(450)
        content_layout.addWidget(widget_1, alignment=Qt.AlignmentFlag.AlignTop)
        content_layout.addWidget(horizontal_line_1, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        # Second Widget
        horizontal_line_2 = QFrame()
        horizontal_line_2.setFrameShape(QFrame.Shape.HLine)
        horizontal_line_2.setFrameShadow(QFrame.Shadow.Sunken)
        horizontal_line_2.setFixedWidth(450)
        widget_2 = Widget(labels['WASTE_TITLE'], [labels['WASTE_QUESTION_1'],
                                                  labels['WASTE_QUESTION_2']])
        self.waste_first_input = widget_2.question_inputs[0]
        self.waste_second_input = widget_2.question_inputs[1]
        content_layout.addWidget(widget_2, alignment=Qt.AlignmentFlag.AlignTop)
        content_layout.addWidget(horizontal_line_2, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        # Third Widget
        widget_3 = Widget(labels['BUSINESS_TRAVEL_TITLE'], [labels['BUSINESS_TRAVEL_QUESTION_1'],
                                                            labels['BUSINESS_TRAVEL_QUESTION_2']])
        self.travel_first_input = widget_3.question_inputs[0]
        self.travel_second_input = widget_3.question_inputs[1]
        content_layout.addWidget(widget_3, alignment=Qt.AlignmentFlag.AlignTop)

        # Buttons
        button_layout = QHBoxLayout()
        clear_button = PushButton(labels['CLEAR_BUTTON'], self.__clear_inputs)
        submit_button = PushButton(labels['SUBMIT_BUTTON'], self.__submit)
        submit_button.setObjectName('Submit')
        button_layout.addWidget(submit_button)
        button_layout.addWidget(clear_button)
        content_layout.addLayout(button_layout)

        self.main_layout.addWidget(content_widget)
        self.main_layout.addWidget(self.loading_widget)

        central_widget.setLayout(self.main_layout)
        pub.subscribe(self.__hide_loading, LLMInterpreter.CHANNEL)

    def __submit(self):
        if not self.energy_first_input.text() or \
                not self.energy_second_input.text() or \
                not self.energy_third_input.text() or \
                not self.waste_first_input.text() or \
                not self.waste_second_input.text() or \
                not self.travel_first_input.text() or \
                not self.travel_second_input.text():
            raise ValueError(labels['EMPTY_INPUT_TITLE'], labels['EMPTY_INPUT_TEXT'])
        else:
            self.__show_loading()
            # Calculate carbon foot print
            energy_usage_dto = EnergyUsage(monthly_electricity_bill=self.energy_first_input.text(),
                                           monthly_natural_gas_bill=self.energy_second_input.text(),
                                           monthly_fuel_bill=self.energy_third_input.text())
            waste_dto = Waste(total_waste_generated_monthly=self.waste_first_input.text(),
                              recycling_percentage=self.waste_second_input.text())
            business_travel_dto = BusinessTravel(total_kilometers_traveled_yearly=self.travel_first_input.text(),
                                                 average_fuel_efficiency=self.travel_second_input.text())
            CarbonFootprint.generate_report(energy_usage_dto, waste_dto, business_travel_dto)

    def __show_loading(self):
        self.main_layout.setCurrentIndex(1)

    def __hide_loading(self, llm_result):
        self.__clear_inputs()
        self.main_layout.setCurrentIndex(0)

    def __clear_inputs(self):
        self.energy_first_input.clear()
        self.energy_second_input.clear()
        self.energy_third_input.clear()
        self.waste_first_input.clear()
        self.waste_second_input.clear()
        self.travel_first_input.clear()
        self.travel_second_input.clear()
