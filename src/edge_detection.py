# src/edge_detection.py
import os
import cv2

def detect_edges(input_dir, output_dir, params):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            edges = cv2.Canny(img, params['threshold1'], params['threshold2'])
            edge_path = os.path.join(output_dir, f'edges_{filename}')
            cv2.imwrite(edge_path, edges)