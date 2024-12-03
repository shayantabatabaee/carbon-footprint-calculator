import os

TEMP_PATH = os.path.join(os.getcwd(), '..', 'temp')
COMPANY_PLOT_PATH = os.path.join(TEMP_PATH, 'company_plot.png')
COMPANY_PDF_PATH = os.path.join(TEMP_PATH, 'company_report.pdf')
FULL_PDF_PATH = os.path.join(TEMP_PATH, 'full_report.pdf')
FULL_PLOT_PATH = os.path.join(TEMP_PATH, 'full_plot.png')
LOADING_PATH = os.path.join(os.getcwd(), 'assets', 'loading.gif')
OPEN_ROUTER_API_KEY = os.getenv('OPEN_ROUTER_API_KEY', '')
