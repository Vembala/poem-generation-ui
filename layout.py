"""layout"""

import pyside2

class VerticalBox(pyside2.QtWidgets.QVBoxLayout):

    """VertivalBox"""

    def __init__(self, text_box: pyside2.QtWidgets.QWidget, output_label: pyside2.QtWidgets.QWidget,):

        """__init__"""

        self.addWidget(text_box,)
        self.addWidget(output_label,)
