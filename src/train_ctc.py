# train_ctc.py
import os
import numpy as np
import tensorflow as tf
from src.model_crnn import create_crnn_model
from src.preprocess import preprocess_image
import string

CHARS = "-" + string.ascii_uppercase + string.digits
char_to_idx = {c: i for i, c in enumerate(CHARS)}
idx_to_char = {i: c for c, i in char_to_idx.items()}

def encode_ctc_label(label):
    return [char_to_idx[c] for c in label]

def load_ctc_dataset(dir_path):
    X, Y, input_lens, label_lens = [], [], [], []
    for file in os.listdir(dir_path):
        label = os.path.splitext(file)[0]
        encoded = encode_ctc_label(label)
        image = preprocess_image(os.path.join(dir_path, file))
        image = np.expand_dims(image, axis=-1)
        X.append(image)
        Y.append(encoded)
        input_lens.append(25)
        label_lens.append(len(encoded))
    return np.array(X), Y, np.array(input_lens), np.array(label_lens)

def train_ctc_model():
    X, Y, input_lens, label_lens = load_ctc_dataset("dataset/train")
    model = create_crnn_model()

    labels = tf.keras.preprocessing.sequence.pad_sequences(Y, maxlen=10, padding='post')
    def ctc_loss_fn(y_true, y_pred):
        return tf.keras.backend.ctc_batch_cost(labels, y_pred, input_lens, label_lens)

    model.compile(loss=ctc_loss_fn, optimizer='adam')
    model.fit(X, labels, epochs=15, batch_size=16)
    model.save("captcha_crnn.h5")
