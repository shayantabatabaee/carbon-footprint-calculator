from typing import Union


class LLMResult:

    def __init__(self, is_successful: bool, result: Union[dict, None], error: Union[Exception, None]):
        self.is_successful = is_successful
        self.result = result
        self.error = error
