import os

from matplotlib import pyplot as plt

from carbon_footprint_calculator.assets.constants import PLOT_PATH, TEMP_PATH


class Plot:

    @staticmethod
    def draw(labels: tuple, sizes: list, colors: list):
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.axis('equal')
        os.makedirs(TEMP_PATH, exist_ok=True)
        plt.savefig(PLOT_PATH)
        plt.close()
