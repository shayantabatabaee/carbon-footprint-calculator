import sys

from PyQt6.QtWidgets import QApplication

from carbon_footprint_calculator.ui.window import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
