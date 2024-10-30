from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit


class Widget(QWidget):

    def __init__(self, label: str, questions: list[str]):
        super().__init__()
        layout = QVBoxLayout()
        heading = QLabel(label)
        layout.addWidget(heading)
        for question in questions:
            question_label = QLabel(question)
            question_input = QLineEdit()
            layout.addWidget(question_label)
            layout.addWidget(question_input)
        self.setLayout(layout)
