# tests/test_feature_extraction.py
import unittest
import os
import numpy as np
from src.feature_extraction import extract_features
import cv2

class TestFeatureExtraction(unittest.TestCase):
    def setUp(self):
        self.input_dir = 'data/test/processed'
        self.params = {'method': 'ORB'}
        os.makedirs(self.input_dir, exist_ok=True)
        
        # Create a dummy processed image
        self.processed_image_path = os.path.join(self.input_dir, 'test_processed.jpg')
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(self.processed_image_path, dummy_image)

    def tearDown(self):
        # Remove features file after tests
        features_path = os.path.join(self.input_dir, 'features.npy')
        if os.path.exists(features_path):
            os.remove(features_path)
            
        # Remove processed test image
        os.remove(self.processed_image_path)
        os.rmdir(self.input_dir)

    def test_extract_features(self):
        extract_features(self.input_dir, self.params)
        features_path = os.path.join(self.input_dir, 'features.npy')
        self.assertTrue(os.path.exists(features_path))
        features = np.load(features_path, allow_pickle=True).item()
        self.assertTrue(len(features) > 0)
        for feature in features.values():
            self.assertIn('keypoints', feature)
            self.assertIn('descriptors', feature)

if __name__ == '__main__':
    unittest.main()