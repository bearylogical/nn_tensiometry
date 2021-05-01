from src.data import load_dataset, extract_txt, extract_labels
import numpy as np
import os

# define directories
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Current file marks the root directory
PARENT_DIR = os.path.dirname(ROOT_DIR)  # Directory for storing logged images
DATA_DIR = os.path.join(PARENT_DIR, "tests", "data")
INDEX_FILE = os.path.join(DATA_DIR, 'index.csv')

# Test functionality of data loaders and utilities
class TestData:
    def test_extract_labels(self):
        assert extract_labels(INDEX_FILE).shape == (3, 2)

    def test_extract_features(self):
        sample_features_file = os.path.join(DATA_DIR, "3.txt")
        assert extract_txt(sample_features_file).shape == (40, 2)

    def test_load_dataset(self):
        features, labels = load_dataset(DATA_DIR, INDEX_FILE)

        # check features
        assert isinstance(features, np.ndarray) 
        assert features.shape == (3, 40, 2)

        # check labels 
        assert isinstance(labels, np.ndarray)
        assert labels.shape == (3, 2)

        