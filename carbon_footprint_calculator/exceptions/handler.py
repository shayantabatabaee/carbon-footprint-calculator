import json
import logging

from httpx import HTTPStatusError, ConnectError
from pydantic_core._pydantic_core import ValidationError

from carbon_footprint_calculator.assets import strings
from carbon_footprint_calculator.ui.message import Message


class Handler:

    @staticmethod
    def handle(exception_type, exception_value, exception_traceback):
        if exception_type is ValueError:
            text = exception_value.args[0]
            informative_text = exception_value.args[1]
        elif exception_type is ValidationError:
            error_json = json.loads(exception_value.json())[0]
            text = error_json["loc"][0]
            informative_text = error_json["msg"]
        elif exception_type is HTTPStatusError:
            text = strings.labels['NETWORK_ERROR']
            informative_text = str(exception_value)
        elif exception_type is ConnectError:
            text = strings.labels['NETWORK_ERROR']
            informative_text = str(exception_value)
        else:
            text = strings.labels['UNKNOWN_ERROR']
            informative_text = strings.labels['UNKNOWN_ERROR_TEXT']

        logging.error(exception_value)
        Message.critical(text, informative_text)

    @staticmethod
    def loop_handler(loop, context):
        Handler.handle(type(context['exception']), context['exception'], None)
