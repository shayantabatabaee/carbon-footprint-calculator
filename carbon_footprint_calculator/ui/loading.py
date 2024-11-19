from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from carbon_footprint_calculator.assets.constants import LOADING_PATH


class Loading(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.loading_label = QLabel(self)
        self.gif = QMovie(LOADING_PATH)
        self.loading_label.setMovie(self.gif)

        layout.addWidget(self.loading_label)
        self.setLayout(layout)

        self.gif.start()
