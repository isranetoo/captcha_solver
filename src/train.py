# train.py
import os
import numpy as np
from src.model import create_model
from src.preprocess import preprocess_image
from src.preprocess import preprocess_image
import tensorflow as tf
import string


CHARS = string.ascii_uppercase + string.digits
char_to_index = {c: i for i, c in enumerate(CHARS)}

def encode_label(label):
    return [tf.keras.utils.to_categorical(char_to_index[c], num_classes=len(CHARS)) for c in label]

def load_dataset(dir_path):
    X, Y = [], []
    for file in os.listdir(dir_path):
        label = os.path.splitext(file)[0]
        image = preprocess_image(os.path.join(dir_path, file))
        image = np.expand_dims(image, axis=-1)
        X.append(image)
        Y.append(encode_label(label))
    X = np.array(X)
    Y = list(map(np.array, zip(*Y)))
    return X, Y

def train_model():
    X_train, Y_train = load_dataset("dataset/train")
    X_test, Y_test = load_dataset("dataset/test")
    model = create_model()
    model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=20, batch_size=32)
    model.save("captcha_model.h5")

if __name__ == "__main__":
    train_model()
