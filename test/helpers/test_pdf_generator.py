import os

import pytest

from carbon_footprint_calculator.assets.constants import COMPANY_PDF_PATH
from carbon_footprint_calculator.helpers.pdf_generator import PDFGenerator


class TestPlot:

    @staticmethod
    @pytest.mark.unit
    def test_generate():
        content = "**This is bold text**"
        PDFGenerator.generate(content, COMPANY_PDF_PATH)
        assert os.path.isfile(COMPANY_PDF_PATH) == True
