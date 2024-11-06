from PyQt6.QtWidgets import QPushButton

from carbon_footprint_calculator.utils.style_sheet import StyleSheet


class PushButton(QPushButton):

    def __init__(self, label, callback=None):
        super().__init__(label)
        self.setStyleSheet(StyleSheet.load_style_sheet('button.css'))
        if callback is not None:
            self.clicked.connect(callback)
