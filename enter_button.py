"""enter_button"""

from PySide2 import QtWidgets

class EnterButton(QtWidgets.QPushButton):

    """EnterButton"""

    def __init__(self, text_generator, text):

        """__init__"""

        super().__init__()

        self.setText(text)
        self.clicked.connect(text_generator.run)
