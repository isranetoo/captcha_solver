
# predict.py
import tensorflow as tf
from src.preprocess import preprocess_image
import numpy as np
import string



CHARS = string.ascii_uppercase + string.digits

def predict(path):
    model = tf.keras.models.load_model("captcha_model.h5")
    image = preprocess_image(path)
    image = np.expand_dims(image, axis=(0, -1))
    pred = model.predict(image)
    return ''.join([CHARS[tf.math.argmax(p).numpy()] for p in pred])
