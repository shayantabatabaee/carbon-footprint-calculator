import asyncio

import pytest
from pubsub import pub

from carbon_footprint_calculator.helpers.llm_interpreter import LLMInterpreter
from carbon_footprint_calculator.models.llm_result import LLMResult


class TestLLMInterpreter:

    @staticmethod
    @pytest.mark.unit
    def test_report():
        result = None
        event = asyncio.Event()

        def on_message_received(llm_result: LLMResult):
            nonlocal result
            result = llm_result
            event.set()

        pub.subscribe(on_message_received, LLMInterpreter.CHANNEL)
        LLMInterpreter.report('Test', 100, 50, 25, 175)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(asyncio.wait_for(event.wait(), timeout=10))
        loop.close()

        assert result is not None, "No message was published to the channel."
        assert result.is_successful is True or result.is_successful is False
        if result.is_successful:
            assert len(result.result['choices'][0]['message']['content']) > 0
        assert isinstance(result, LLMResult)
