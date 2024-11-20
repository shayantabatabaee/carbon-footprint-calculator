from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QMainWindow

from carbon_footprint_calculator.assets.strings import labels


class PDFViewerWindow(QMainWindow):

    def __init__(self, pdf_path: str):
        super().__init__()

        self.setFixedSize(768, 1024)
        self.setWindowTitle(labels['PDF_VIEWER_WINDOW_TITLE'])

        self.web_view = QWebEngineView(self)
        self.web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.PdfViewerEnabled, True)

        self.web_view.setUrl(QUrl.fromLocalFile(pdf_path))
        self.setCentralWidget(self.web_view)
