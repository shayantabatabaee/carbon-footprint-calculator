import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFrame, QSizePolicy, QLayout, QLabel

from carbon_footprint_calculator.assets.strings import labels
from carbon_footprint_calculator.ui.widget import Widget


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(550, 650)
        self.setWindowTitle(labels['WINDOW_TITLE'])
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        image_path = os.path.join(os.getcwd(), 'assets', 'logo.png')
        logo_label = QLabel()

        logo_image = QPixmap(image_path)
        logo_label.setPixmap(logo_image)
        main_layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        # First Widget
        widget_1 = Widget(labels['ENERGY_USAGE_TITLE'], [labels['ENERGY_USAGE_QUESTION_1'],
                                                         labels['ENERGY_USAGE_QUESTION_2'],
                                                         labels['ENERGY_USAGE_QUESTION_3']])
        horizontal_line_1 = QFrame()
        horizontal_line_1.setFrameShape(QFrame.Shape.HLine)
        horizontal_line_1.setFrameShadow(QFrame.Shadow.Sunken)
        horizontal_line_1.setFixedWidth(450)
        main_layout.addWidget(widget_1, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addWidget(horizontal_line_1, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        # Second Widget
        horizontal_line_2 = QFrame()
        horizontal_line_2.setFrameShape(QFrame.Shape.HLine)
        horizontal_line_2.setFrameShadow(QFrame.Shadow.Sunken)
        horizontal_line_2.setFixedWidth(450)
        widget_2 = Widget(labels['WASTE_TITLE'], [labels['WASTE_QUESTION_1'],
                                                  labels['WASTE_QUESTION_2']])
        main_layout.addWidget(widget_2, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addWidget(horizontal_line_2, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        # Third Widget
        widget_3 = Widget(labels['BUSINESS_TRAVEL_TITLE'], [labels['BUSINESS_TRAVEL_QUESTION_1'],
                                                            labels['BUSINESS_TRAVEL_QUESTION_2']])
        main_layout.addWidget(widget_3, alignment=Qt.AlignmentFlag.AlignTop)

        central_widget.setLayout(main_layout)
