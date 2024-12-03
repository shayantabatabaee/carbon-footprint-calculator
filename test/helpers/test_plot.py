import os

import numpy as np
import pytest

from carbon_footprint_calculator.assets.constants import COMPANY_PLOT_PATH, FULL_PLOT_PATH
from carbon_footprint_calculator.helpers.plot import Plot


class TestPlot:

    @staticmethod
    @pytest.mark.unit
    def test_draw_pie_chart():
        labels = ('Label 1', 'Label 2')
        sizes = [1, 1]
        colors = ['#dedce5', '#dfe6ee']
        Plot.draw_pie_chart(labels, sizes, colors, COMPANY_PLOT_PATH)
        assert os.path.isfile(COMPANY_PLOT_PATH) == True

    @staticmethod
    @pytest.mark.unit
    def test_draw_bar_chart():
        labels = ['Company 1', 'Company 2']
        weights_count = {
            'Energy Usage': np.array([1, 2]),
            'Generated Waste': np.array([2, 3]),
            'Business Travel Usage': np.array([3, 4])
        }
        Plot.draw_bar_chart(labels, weights_count, FULL_PLOT_PATH)
        assert os.path.isfile(FULL_PLOT_PATH) == True
