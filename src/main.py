# src/main.py

import os
from src.config import load_config
from src.augmentation import augment_images
from src.edge_detection import detect_edges
from src.object_detection import detect_objects
from src.feature_extraction import extract_features
from src.fetch_images import fetch_images_from_pexels  # Ensure only Pexels is imported

def main():
    config = load_config()
    raw_dir = config['directories'].get('raw', 'data/raw')
    augmented_dir = config['directories'].get('augmented', 'data/augmented')
    processed_dir = config['directories'].get('processed', 'data/processed')
    
    # Pexels related configurations
    pexels_config = config.get('pexels', {})
    queries = pexels_config.get('queries', [])
    per_page = pexels_config.get('per_page', 5)
    api_key = pexels_config.get('api_key', '')
    
    # Fetch Images from Pexels
    if api_key and queries:
        for query in queries:
            print(f"Fetching images for query: '{query}'")
            fetch_images_from_pexels(query, per_page, api_key, raw_dir)
    else:
        print("Pexels configuration is incomplete. Skipping image fetching.")
    
    # Augment Images
    augment_images(raw_dir, augmented_dir, config.get('augmentation', {}))
    print("Image augmentation completed.")
    
    # Edge Detection
    detect_edges(augmented_dir, processed_dir, config.get('edge_detection', {}))
    print("Edge detection completed.")
    
    # Object Detection
    detect_objects(processed_dir, config.get('object_detection', {}))
    print("Object detection completed.")
    
    # Feature Extraction
    extract_features(processed_dir, config.get('feature_extraction', {}))
    print("Feature extraction completed.")

if __name__ == '__main__':
    main()