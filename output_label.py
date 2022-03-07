"""output_label"""

from PySide2 import QtWidgets

class OutputLabel(QtWidgets.QLabel):

    """OutputLabel"""

    def __init__(self,):

        """__init__"""

        super().__init__()

        self.setStyleSheet("background-color: white")
