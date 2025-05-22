# preprocess.py
import cv2
import numpy as np

def preprocess_image(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (200, 60))
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    filtered = cv2.medianBlur(thresh, 3)
    return filtered / 255.0
