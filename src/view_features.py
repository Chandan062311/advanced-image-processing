# src/view_features.py
import numpy as np

def view_features(features_path):
    features = np.load(features_path, allow_pickle=True).item()
    for image, feature in features.items():
        print(f"Image: {image}")
        print(f"  Keypoints: {feature['keypoints']}")
        print(f"  Descriptors Shape: {feature['descriptors']}")
        print("-" * 30)

if __name__ == "__main__":
    features_path = 'data/processed/features.npy'
    view_features(features_path)