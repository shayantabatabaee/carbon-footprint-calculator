from PyQt6.QtWidgets import QMainWindow

from carbon_footprint_calculator.assets.strings import titles


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(titles['WINDOW_TITLE'])
