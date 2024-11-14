# src/feature_extraction.py
import os
import cv2
import numpy as np

def extract_features(input_dir, params):
    features = {}
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            orb = cv2.ORB_create()
            keypoints, descriptors = orb.detectAndCompute(img, None)
            features[filename] = {
                'keypoints': len(keypoints),
                'descriptors': descriptors.shape if descriptors is not None else 0
            }
    # Save features to a file
    np.save(os.path.join(input_dir, 'features.npy'), features)