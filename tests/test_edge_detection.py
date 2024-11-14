# tests/test_edge_detection.py
import unittest
import os
from src.edge_detection import detect_edges
import cv2
import numpy as np

class TestEdgeDetection(unittest.TestCase):
    def setUp(self):
        self.input_dir = 'data/test/augmented'
        self.output_dir = 'data/test/processed'
        self.params = {'threshold1': 50, 'threshold2': 150}
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Create a dummy augmented image
        self.augmented_image_path = os.path.join(self.input_dir, 'test_augmented.jpg')
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(self.augmented_image_path, dummy_image)

    def tearDown(self):
        # Clean up processed directory after tests
        for f in os.listdir(self.output_dir):
            os.remove(os.path.join(self.output_dir, f))
        os.rmdir(self.output_dir)
        
        # Remove augmented test image
        os.remove(self.augmented_image_path)
        os.rmdir(self.input_dir)

    def test_detect_edges(self):
        detect_edges(self.input_dir, self.output_dir, self.params)
        self.assertTrue(os.path.exists(self.output_dir))
        self.assertTrue(len(os.listdir(self.output_dir)) > 0)

if __name__ == '__main__':
    unittest.main()