# tests/test_augmentation.py
import unittest
import os
from src.augmentation import augment_images
import cv2
import numpy as np

class TestAugmentation(unittest.TestCase):
    def setUp(self):
        self.input_dir = 'data/test/raw'
        self.output_dir = 'data/test/augmented'
        self.params = {'rotate': 10, 'flip': True}
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Create a dummy image
        self.test_image_path = os.path.join(self.input_dir, 'test.jpg')
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(self.test_image_path, dummy_image)

    def tearDown(self):
        # Clean up augmented directory after tests
        for f in os.listdir(self.output_dir):
            os.remove(os.path.join(self.output_dir, f))
        os.rmdir(self.output_dir)
        
        # Remove raw test image
        os.remove(self.test_image_path)
        os.rmdir(self.input_dir)

    def test_augment_images(self):
        augment_images(self.input_dir, self.output_dir, self.params)
        self.assertTrue(os.path.exists(self.output_dir))
        self.assertTrue(len(os.listdir(self.output_dir)) > 0)

if __name__ == '__main__':
    unittest.main()