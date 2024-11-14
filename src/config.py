# src/config.py

import yaml
import os

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
        # Get the directory of the current file (src)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Navigate to the parent directory to find 'configs/config.yaml'
        config_path = os.path.join(current_dir, '..', 'configs', 'config.yaml')

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return config