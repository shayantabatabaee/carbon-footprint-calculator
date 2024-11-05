import os


class StyleSheet:

    @staticmethod
    def load_style_sheet(file_name: str) -> str:
        with open(os.path.join(os.getcwd(), 'ui/css', file_name), 'r') as stylesheet:
            return stylesheet.read()
