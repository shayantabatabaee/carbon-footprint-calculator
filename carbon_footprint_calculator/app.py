import asyncio
import logging
import sys

from PyQt6.QtWidgets import QApplication
from qasync import QEventLoop

from carbon_footprint_calculator.exceptions.handler import Handler
from carbon_footprint_calculator.ui.window import Window

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    window = Window()
    window.show()

    sys.excepthook = Handler.handle
    loop.set_exception_handler(Handler.loop_handler)

    try:
        with loop:
            loop.run_forever()
    finally:
        loop.close()


    sys.exit(loop.close())
