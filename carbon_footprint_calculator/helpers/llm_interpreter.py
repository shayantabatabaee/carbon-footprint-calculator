import asyncio
from typing import Callable

import httpx

from carbon_footprint_calculator.assets import constants
from carbon_footprint_calculator.models.llm_result import LLMResult


class LLMInterpreter:
    __OPEN_ROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
    __API_KEY = constants.OPEN_ROUTER_API_KEY
    __TIMEOUT = 60  # In seconds

    @staticmethod
    def report(energy_usage: float, generated_waste: float, business_travel_usage: float, callback: Callable = None):
        async def call():
            total_usage = energy_usage + generated_waste + business_travel_usage
            prompt = [
                {
                    "role": "system",
                    "content": "You are an assistant for generating report for carbon footprint calculator application,"
                               " the user will give you data regarding the energy usages, generated wastes and business travels"
                               " for one year for a company in kgCO2 unit. You have to generate a report to"
                               " compare these numbers together and also help the company that in which ways can reduce these"
                               " numbers to reduce carbon generation. you do not know anything about the company name"
                               " and please avoid using place holders in your report. Try your best!"
                },
                {
                    "role": "user",
                    "content": f"Here are the numbers for generating report, "
                               f"Energy Usage: {energy_usage}, percent: {(energy_usage * 100) / total_usage}"
                               f"Generated Waste: {generated_waste}, percent: {(generated_waste * 100) / total_usage}"
                               f"Business Travel Usage: {business_travel_usage}, percent: {(business_travel_usage * 100) / total_usage}"
                               f"Total Usage: {total_usage}"
                }
            ]
            body = {
                "model": "meta-llama/llama-3.1-70b-instruct:free",
                "messages": prompt
            }
            headers = {"Authorization": f"Bearer {LLMInterpreter.__API_KEY}"}

            async with httpx.AsyncClient(trust_env=False, timeout=LLMInterpreter.__TIMEOUT) as client:
                try:
                    response = await client.post(LLMInterpreter.__OPEN_ROUTER_URL, json=body, headers=headers)
                    response.raise_for_status()
                    data = response.json()
                    result: LLMResult = LLMResult(is_successful=True, result=data, error=None)
                except Exception as e:
                    result: LLMResult = LLMResult(is_successful=False, result=None, error=e)

            if callback:
                callback(result)

        asyncio.run(call())
