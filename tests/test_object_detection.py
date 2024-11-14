# tests/test_object_detection.py
import unittest
import os
import shutil
from src.object_detection import detect_objects
import cv2
import numpy as np

class TestObjectDetection(unittest.TestCase):
    def setUp(self):
        self.input_dir = 'data/test/processed'
        self.params = {
            'cascade': 'haarcascade_frontalface_default.xml',
            'color': [0, 255, 0],
            'thickness': 2
        }
        os.makedirs(self.input_dir, exist_ok=True)
        
        # Create a dummy processed image
        self.processed_image_path = os.path.join(self.input_dir, 'test_processed.jpg')
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(self.processed_image_path, dummy_image)
        
        # Ensure cascade file exists
        cascade_src = os.path.join('configs', 'haarcascade_frontalface_default.xml')
        if not os.path.exists(cascade_src):
            raise FileNotFoundError(f"Cascade file not found: {cascade_src}")
        
    def tearDown(self):
        # Remove detected files after tests
        for f in os.listdir(self.input_dir):
            if f.startswith('detected_'):
                os.remove(os.path.join(self.input_dir, f))
        
        # Remove processed test image
        os.remove(self.processed_image_path)
        os.rmdir(self.input_dir)

    def test_detect_objects(self):
        detect_objects(self.input_dir, self.params)
        detected_files = [f for f in os.listdir(self.input_dir) if f.startswith('detected_')]
        self.assertTrue(len(detected_files) > 0)

if __name__ == '__main__':
    unittest.main()