import os

from markdown import markdown
from xhtml2pdf import pisa

from carbon_footprint_calculator.assets.constants import PDF_PATH, TEMP_PATH


class PDFGenerator:

    @staticmethod
    def generate(markdown_content: str):
        os.makedirs(TEMP_PATH, exist_ok=True)
        html_content = markdown(markdown_content)
        with open(PDF_PATH, "wb") as pdf_file:
            pisa.CreatePDF(html_content, dest=pdf_file)
