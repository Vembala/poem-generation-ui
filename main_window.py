"""main_window"""

from PySide2 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    """MainWindow"""

    def __init__(self, central_widget: QtWidgets.QWidget,):

        """__init__"""

        self.setCentralWidget(central_widget)
