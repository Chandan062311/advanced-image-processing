# src/object_detection.py
import os
import cv2

def detect_objects(input_dir, params):
    # Initialize pre-trained model (e.g., Haar Cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + params['cascade'])
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            objects = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in objects:
                cv2.rectangle(img, (x, y), (x+w, y+h), params['color'], params['thickness'])
            detection_path = os.path.join(input_dir, f'detected_{filename}')
            cv2.imwrite(detection_path, img)