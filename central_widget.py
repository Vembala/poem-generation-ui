"""central_widget"""

import pyside2

class CentralWidget(pyside2.QtWidgets.QWidget):

    """CentralWidget"""

    def __init__(self, layout: pyside2.QtWidgets.QLayout):

        """__init__"""

        super().__init__()

        self.setLayout(layout)
