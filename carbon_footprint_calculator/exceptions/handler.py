from carbon_footprint_calculator.ui.message import Message


class Handler:

    @staticmethod
    def handle(exception_type, exception_value, exception_traceback):
        if exception_type is ValueError:
            text = exception_value.args[0]
            informative_text = exception_value.args[1]
            Message.critical(text, informative_text)
