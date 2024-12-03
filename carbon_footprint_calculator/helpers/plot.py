import os

import numpy as np
from matplotlib import pyplot as plt

from carbon_footprint_calculator.assets.constants import TEMP_PATH


class Plot:

    @staticmethod
    def draw_pie_chart(labels: tuple, sizes: list, colors: list, path: str):
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.axis('equal')
        os.makedirs(TEMP_PATH, exist_ok=True)
        plt.savefig(path)
        plt.close()

    @staticmethod
    def draw_bar_chart(labels: list, weight_counts: dict, path: str):
        fig, ax = plt.subplots()

        bottom = np.zeros(len(labels))
        for key, value in weight_counts.items():
            ax.bar(labels, value, 0.4, label=key, bottom=bottom)
            bottom += value

        ax.set_title("Companies Carbon Footprint Usage")
        ax.legend(loc="upper right")
        os.makedirs(TEMP_PATH, exist_ok=True)
        plt.savefig(path)
        plt.close()
