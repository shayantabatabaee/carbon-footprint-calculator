import os

TEMP_PATH = os.path.join(os.getcwd(), '..', 'temp')
PLOT_PATH = os.path.join(TEMP_PATH, 'plot.png')
PDF_PATH = os.path.join(TEMP_PATH, 'report.pdf')
LOADING_PATH = os.path.join(os.getcwd(), 'assets', 'loading.gif')
OPEN_ROUTER_API_KEY = os.getenv('OPEN_ROUTER_API_KEY', '')
