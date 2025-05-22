
# model.py
import tensorflow as tf

def create_model(num_chars=6, num_classes=36):
    inputs = tf.keras.layers.Input(shape=(60, 200, 1))
    x = tf.keras.layers.Conv2D(32, (3,3), activation='relu')(inputs)
    x = tf.keras.layers.MaxPooling2D(2,2)(x)
    x = tf.keras.layers.Conv2D(64, (3,3), activation='relu')(x)
    x = tf.keras.layers.MaxPooling2D(2,2)(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    outputs = [tf.keras.layers.Dense(num_classes, activation='softmax', name=f"char_{i}")(x) for i in range(num_chars)]
    model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
