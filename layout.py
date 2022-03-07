"""layout"""

from PySide2 import QtWidgets

class VerticalBox(QtWidgets.QVBoxLayout):

    """VertivalBox"""

    def __init__(self, text_box: QtWidgets.QWidget, output_label: QtWidgets.QWidget,):

        """__init__"""

        super().__init__()

        self.addWidget(text_box,)
        self.addWidget(output_label,)
