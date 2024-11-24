import os

import pytest

from carbon_footprint_calculator.assets.constants import PDF_PATH
from carbon_footprint_calculator.helpers.pdf_generator import PDFGenerator


class TestPlot:

    @staticmethod
    @pytest.mark.unit
    def test_generate():
        content = "**This is bold text**"
        PDFGenerator.generate(content)
        assert os.path.isfile(PDF_PATH) == True
