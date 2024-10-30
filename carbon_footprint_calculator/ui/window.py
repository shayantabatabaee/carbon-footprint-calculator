from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from carbon_footprint_calculator.assets.strings import labels
from carbon_footprint_calculator.ui.widget import Widget


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(labels['WINDOW_TITLE'])
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        widget_1 = Widget(labels['ENERGY_USAGE_TITLE'], [labels['ENERGY_USAGE_QUESTION_1'],
                                                         labels['ENERGY_USAGE_QUESTION_2'],
                                                         labels['ENERGY_USAGE_QUESTION_3']])
        main_layout.addWidget(widget_1)

        widget_2 = Widget(labels['WASTE_TITLE'], [labels['WASTE_QUESTION_1'],
                                                  labels['WASTE_QUESTION_2']])
        main_layout.addWidget(widget_2)

        widget_3 = Widget(labels['BUSINESS_TRAVEL_TITLE'], [labels['BUSINESS_TRAVEL_QUESTION_1'],
                                                            labels['BUSINESS_TRAVEL_QUESTION_2']])
        main_layout.addWidget(widget_3)

        central_widget.setLayout(main_layout)
