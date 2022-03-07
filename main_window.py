"""main_window"""

import PySide2 as pyside2

class MainWindow(pyside2.QtWidgets.QMainWindow):

    """MainWindow"""

    def __init__(self, central_widget: pyside2.QtWidgets.QWidget,):

        """__init__"""

        self.setCentralWidget(central_widget)
