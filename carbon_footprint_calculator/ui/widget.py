from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QGridLayout, QSizePolicy, QHBoxLayout, QLayout

from carbon_footprint_calculator.utils.style_sheet import StyleSheet


class Widget(QWidget):

    def __init__(self, label: str, questions: list[str]):
        super().__init__()
        self.setStyleSheet(StyleSheet.load_style_sheet('widget.css'))
        layout = QVBoxLayout()

        heading = QLabel(label)
        heading.setObjectName('Heading')
        layout.addWidget(heading, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        for i in range(len(questions)):
            question_layout = QHBoxLayout()

            question_label = QLabel(questions[i])
            question_label.setWordWrap(True)
            question_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

            question_input = QLineEdit()
            question_input.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            question_input.setFixedWidth(100)

            question_layout.addWidget(question_label, stretch=1)
            question_layout.addWidget(question_input, alignment=Qt.AlignmentFlag.AlignRight)

            layout.addLayout(question_layout)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setLayout(layout)
