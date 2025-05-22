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
    # Always return 5 elements, pad with zeros if label is shorter
    encoded = [tf.keras.utils.to_categorical(char_to_index[c], num_classes=len(CHARS)) for c in label]
    while len(encoded) < 5:
        encoded.append(np.zeros(len(CHARS)))
    return encoded

def load_dataset(dir_path):
    X, Y = [], []
    for file in os.listdir(dir_path):
        label = os.path.splitext(file)[0]
        img_path = os.path.join(dir_path, file)
        # Só aceita labels de 5 caracteres alfanuméricos
        if not (len(label) == 5 and label.isalnum()):
            print(f"[AVISO] Ignorando arquivo '{img_path}': nome de arquivo inválido")
            continue
        try:
            label_up = label.upper()
            image = preprocess_image(img_path)
            image = np.expand_dims(image, axis=-1)
            Y.append(encode_label(label_up))
            X.append(image)
        except Exception as e:
            print(f"[AVISO] Ignorando arquivo '{img_path}': {e}")
            continue
    if not X:
        raise RuntimeError(f"Nenhuma imagem válida encontrada em {dir_path}")
    X = np.array(X)
    Y = list(map(np.array, zip(*Y)))
    return X, Y

def train_model():
    X_train, Y_train = load_dataset("dataset/train")
    X_test, Y_test = load_dataset("dataset/test")
    model = create_model(num_chars=5, num_classes=len(CHARS))
    model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=20, batch_size=32)
    model.save("captcha_model.h5")

if __name__ == "__main__":
    train_model()
