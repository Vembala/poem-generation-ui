"""text_box"""

from PySide2 import QtWidgets

class TextBox(QtWidgets.QTextEdit):

    """TextBox"""

    def __init__(self, text_generator):

        """__init__"""

        super().__init__()

        self.toPlainText.connect(text_generator.run)
