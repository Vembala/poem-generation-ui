"""main"""

import pickle
import tensorflow as tf
from text_box import TextBox
from output_label import OutputLabel
from layout import VerticalBox
from central_widget import CentralWidget
from text_generator import TextGenerator

VOCAB_PATH = "vocab.pkl"
READ_BYTE_MODE = "rb"
LINES = 10
MAXLEN = 80
MAXTOKENS = 6
MODEL_PATH = "model"

with open(VOCAB_PATH, READ_BYTE_MODE) as file:
    vocab = pickle.load(file)

model = tf.keras.models.load_model(MODEL_PATH)

output_label = OutputLabel()
text_generator = TextGenerator(output_label, vocab, LINES, MAXLEN, MAXTOKENS, MODEL_PATH)
text_box = TextBox(text_generator)
vertical_box = VerticalBox(text_box, output_label,)
central_widget = CentralWidget(vertical_box,)
