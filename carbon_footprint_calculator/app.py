import logging
import sys

from PyQt6.QtWidgets import QApplication

from carbon_footprint_calculator.exceptions.handler import Handler
from carbon_footprint_calculator.ui.window import Window

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.excepthook = Handler.handle
    sys.exit(app.exec())
