
# Advanced Image Processing Pipeline

## Project Overview

The **Advanced Image Processing Pipeline** is an automated system designed for image acquisition, augmentation, processing, and analysis using various computer vision techniques. This pipeline leverages the Pexels API for image retrieval and performs tasks such as edge detection, object detection, and feature extraction, offering a complete suite for image analysis and machine learning projects.

---

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Running the Scripts](#running-the-scripts)
8. [Data Directories](#data-directories)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

---

## Features

- **Image Acquisition:** Fetches high-quality images based on predefined queries using the Pexels API.
- **Image Augmentation:** Applies transformations (rotation, flipping) to diversify the dataset.
- **Edge Detection:** Uses the Canny algorithm to detect and highlight significant edges.
- **Object Detection:** Identifies objects like faces using Haar Cascade classifiers.
- **Feature Extraction:** Extracts image keypoints and descriptors using ORB for further analysis.
- **Feature Visualization:** Visualizes extracted features to verify processing accuracy.

---

## Technologies Used

- **Programming Language:** Python 3.9
- **Libraries & Frameworks:** OpenCV, NumPy, PyYAML, Scikit-Image, Matplotlib, Requests, Pillow
- **Version Control:** Git & GitHub

---

## Project Structure

```
advanced-image-processing/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── fetch_images.py
│   ├── augmentation.py
│   ├── edge_detection.py
│   ├── object_detection.py
│   ├── feature_extraction.py
│   ├── view_features.py
│   └── main.py
├── configs/
│   └── config.yaml
├── data/
│   ├── raw/
│   ├── augmented/
│   └── processed/
├── tests/
│   └── test_config.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/advanced-image-processing.git
   cd advanced-image-processing
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Configure API Keys:**  
   Create a `.env` file in the root directory to securely store your API keys:
   ```plaintext
   PEXELS_API_KEY=your_pexels_api_key_here
   ```

2. **Update `config.yaml`:**  
   Edit `configs/config.yaml` to set desired configurations, including data directories, augmentation parameters, and API query settings.

---

## Usage

1. **Fetch Images:** Run the script to download images based on configured search queries:
   ```bash
   python -m src.fetch_images
   ```

2. **Process Images:** Execute the main processing pipeline:
   ```bash
   python -m src.main
   ```

3. **View Extracted Features:** Inspect extracted features like keypoints and descriptors:
   ```bash
   python -m src.view_features
   ```

---

## Running the Scripts

1. **`fetch_images.py`:** Fetches images from Pexels.
2. **`main.py`:** Orchestrates the entire pipeline (augmentation, edge detection, object detection, feature extraction).
3. **`view_features.py`:** Displays the extracted features.

---

## Data Directories

- **`data/raw/`:** Original images from Pexels.
- **`data/augmented/`:** Images after transformations.
- **`data/processed/`:** Images after edge detection, object detection, and feature extraction.

---

## Contributing

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

---

## License

This project is licensed under the MIT License.

---

## Contact

For inquiries or support:
- **Email:** chandansatwani422@gmail.com
- **GitHub:** https://github.com/Chandan062311