# evaluate.py
import tensorflow as tf
from src.train import load_dataset, CHARS
import numpy as np

def evaluate():
    model = tf.keras.models.load_model("captcha_model.h5")
    X_test, Y_test = load_dataset("dataset/test")
    correct = 0
    for i in range(len(X_test)):
        pred = model.predict(np.expand_dims(X_test[i], axis=0))
        pred_text = ''.join([CHARS[tf.math.argmax(p).numpy()] for p in pred])
        true_text = ''.join([CHARS[tf.math.argmax(c).numpy()] for c in Y_test[i]])
        if pred_text == true_text:
            correct += 1
    print(f"Acurácia: {correct / len(X_test) * 100:.2f}%")
