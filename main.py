"""main"""

import pickle
import tensorflow as tf
from text_box import TextBox
from output_label import OutputLabel
from layout import VerticalBox
from central_widget import CentralWidget
from text_generator import TextGenerator
from main_window import MainWindow
from PySide2 import QtWidgets
import sys
from custom_object import TokenAndPositionEmbedding
from enter_button import EnterButton

app = QtWidgets.QApplication([])

VOCAB_PATH = "vocab.pkl"
READ_BYTE_MODE = "rb"
LINES = 10
MAXLEN = 80
MAXTOKENS = 6
MODEL_PATH = "model"
CUSTOM_OBJECT = "TokenAndPositionEmbedding"
K = 20000
BUTTON_NAME = "Enter"

with open(VOCAB_PATH, READ_BYTE_MODE) as file:
    vocab = pickle.load(file)

model = tf.keras.models.load_model(MODEL_PATH, custom_objects={CUSTOM_OBJECT: TokenAndPositionEmbedding})

output_label = OutputLabel()
text_box = TextBox()
text_generator = TextGenerator(text_box, output_label, vocab, LINES, MAXLEN, MAXTOKENS, model, K)
enter_button = EnterButton(text_generator, BUTTON_NAME)
vertical_box = VerticalBox(text_box, enter_button, output_label,)
central_widget = CentralWidget(vertical_box,)
main_window = MainWindow(central_widget)

main_window.show()
sys.exit(app.exec_())
