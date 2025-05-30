
# export.py
import tensorflow as tf

def export_to_tflite(model_path, output_path):
    model = tf.keras.models.load_model(model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    with open(output_path, 'wb') as f:
        f.write(tflite_model)

if __name__ == "__main__":
    export_to_tflite("captcha_model.h5", "captcha_model.tflite")
