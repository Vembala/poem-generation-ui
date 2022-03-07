"""text_box"""

import pyside2

class TextBox(pyside2.QtWidgets.QTextEdit):

    """TextBox"""

    def __init__(self, text_generator):

        """__init__"""

        self.textChanged.connect(text_generator.run)
