# src/fetch_images.py

import os
import requests
import sys
import yaml
import time

def load_config(config_path=None):
    """
    Load the YAML configuration file.

    Args:
        config_path (str, optional): Path to the configuration file.
                                      If None, defaults to 'configs/config.yaml' relative to the project root.

    Returns:
        dict: Configuration parameters.
    """
    if config_path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, '..', 'configs', 'config.yaml')

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return config

def fetch_images_from_pexels(query, per_page, api_key, download_dir, max_retries=3):
    """
    Fetch images from Pexels based on a search query.

    Args:
        query (str): Search keyword.
        per_page (int): Number of images to fetch.
        api_key (str): Pexels API Key.
        download_dir (str): Directory to save downloaded images.
        max_retries (int): Maximum number of retries for API requests.

    Returns:
        None
    """
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    url = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": api_key
    }
    params = {
        "query": query,
        "per_page": per_page
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, params=params)
            if (response.status_code == 200):
                break
            elif response.status_code == 429:
                print("Rate limit exceeded. Waiting for 60 seconds before retrying...")
                time.sleep(60)
            else:
                print(f"Error fetching images: {response.status_code} - {response.text}")
                return
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return
    else:
        print("Max retries exceeded. Skipping this query.")
        return

    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        print(f"No images found for query: '{query}'")
        return

    for idx, photo in enumerate(photos):
        image_url = photo['src']['large']
        image_extension = image_url.split('?')[0].split('.')[-1]
        image_path = os.path.join(download_dir, f"{query}_{idx+1}.{image_extension}")

        try:
            img_response = requests.get(image_url)
            img_response.raise_for_status()
            with open(image_path, 'wb') as handler:
                handler.write(img_response.content)
            print(f"Downloaded {image_path}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {image_url}: {e}")

def main():
    """
    Main function to fetch images based on configurations.
    """
    config = load_config()

    pexels_config = config.get('pexels', {})
    queries = pexels_config.get('queries', [])
    per_page = pexels_config.get('per_page', 5)
    api_key = pexels_config.get('api_key', '')

    if not api_key:
        print("Pexels API Key is missing in the configuration.")
        sys.exit(1)

    if not queries:
        print("No queries found in the configuration. Please add search queries under 'pexels'.")
        sys.exit(1)

    raw_dir = config['directories'].get('raw', 'data/raw')

    for query in queries:
        print(f"Fetching images for query: '{query}'")
        fetch_images_from_pexels(query, per_page, api_key, raw_dir)

if __name__ == "__main__":
    main()