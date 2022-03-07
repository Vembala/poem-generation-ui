"""text_generator"""

import PySide2 as pyside2
import numpy as np
import tensorflow as tf

class TextGenerator(pyside2.QtWidgets.QWidget):

    """TextGenerator"""

    def __init__(self, output_label: pyside2.QtWidgets.QLabel, vocab, lines, maxlen, max_tokens, model):

        """__init__"""

        self.text_box = text_box
        self.lines = lines
        self.maxlen = maxlen
        self.max_tokens = max_tokens
        self.model = model
        self.output_label = output_label
        self.word_to_index = {}
        for index, word in enumerate(vocab):
            self.word_to_index[word] = index

    def sample_from(self, logits):
        logits, indices = tf.math.top_k(logits, k=k, sorted=True)
        indices = np.asarray(indices).astype("int32")
        preds = tf.keras.activations.softmax(tf.expand_dims(logits, 0))[0]
        preds = np.asarray(preds).astype("float32")
        return np.random.choice(indices, p=preds)

    def detokenize(self, number):
        return self.vocab[number]

    def run(self, start_prompt,):

        """run"""

        texts = []
        for _ in range(self.lines):
            start_tokens = [self.word_to_index.get(_, 1) for _ in start_prompt.split()]
            num_tokens_generated = 0
            tokens_generated = []
            start_tokens_ = [_ for _ in start_tokens]
            while num_tokens_generated <= self.max_tokens:
                pad_len = self.maxlen - len(start_tokens_)
                sample_index = len(start_tokens_) - 1
                if pad_len < 0:
                    x = start_tokens_[:self.maxlen]
                    sample_index = self.maxlen - 1
                elif pad_len > 0:
                    x = start_tokens_ + [0] * pad_len
                else:
                    x = start_tokens_
                x = np.array([x])
                y, _ = self.model.predict(x)
                sample_token = self.sample_from(y[0][sample_index])
                tokens_generated.append(sample_token)
                start_tokens_.append(sample_token)
            num_tokens_generated = len(tokens_generated)
            txt = " ".join([self.detokenize(_) for _ in start_tokens + tokens_generated])
            texts.append(txt)
            start_prompt = " ".join(txt.split()[-1:])
        plain_text = " ".join(texts)
        self.output_label.setText(plain_text)
