import os

import pytest

from carbon_footprint_calculator.assets.constants import PLOT_PATH
from carbon_footprint_calculator.helpers.plot import Plot


class TestPlot:

    @staticmethod
    @pytest.mark.unit
    def test_draw():
        labels = ('Label 1', 'Label 2')
        sizes = [1, 1]
        colors = ['#dedce5', '#dfe6ee']
        Plot.draw(labels, sizes, colors)
        assert os.path.isfile(PLOT_PATH) == True
