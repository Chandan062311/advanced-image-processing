# src/augmentation.py
import os
import cv2
import numpy as np

def augment_images(input_dir, output_dir, params):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path)
            if img is not None:
                # Example augmentations
                rotated = rotate_image(img, params.get('rotate', 0))
                flipped = flip_image(rotated, params.get('flip', False))
                augmented_path = os.path.join(output_dir, filename)
                cv2.imwrite(augmented_path, flipped)

def rotate_image(image, angle):
    if angle == 0:
        return image
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h))

def flip_image(image, horizontal=True):
    if horizontal:
        return cv2.flip(image, 1)
    return image