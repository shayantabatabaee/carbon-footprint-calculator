import asyncio
import logging
import os
import sys

from PyQt6.QtWidgets import QApplication
from qasync import QEventLoop

sys.path.append(os.path.join(os.getcwd(), '..'))

from carbon_footprint_calculator.exceptions.handler import Handler
from carbon_footprint_calculator.ui.main_window import MainWindow

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    window = MainWindow()
    window.show()

    sys.excepthook = Handler.handle
    loop.set_exception_handler(Handler.loop_handler)

    try:
        with loop:
            loop.run_forever()
    finally:
        loop.close()


    sys.exit(loop.close())
