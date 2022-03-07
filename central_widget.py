"""central_widget"""

from PySide2 import QtWidgets

class CentralWidget(QtWidgets.QWidget):

    """CentralWidget"""

    def __init__(self, layout: QtWidgets.QLayout):

        """__init__"""

        super().__init__()

        self.setLayout(layout)
