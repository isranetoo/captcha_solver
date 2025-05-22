# augment.py
import cv2
import numpy as np
import albumentations as A

def augment_image(image):
    transform = A.Compose([
        A.GaussianBlur(p=0.2),
        A.RandomBrightnessContrast(p=0.3),
        A.ShiftScaleRotate(shift_limit=0.02, scale_limit=0.02, rotate_limit=15, p=0.5),
        A.ImageCompression(quality_lower=70, p=0.3)
    ])
    return transform(image=image)["image"]
