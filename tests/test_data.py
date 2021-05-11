from src.data import extract_features, load_dataset, extract_labels
import numpy as np
import os

# define directories
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Current file marks the root directory
PARENT_DIR = os.path.dirname(ROOT_DIR)  # Directory for storing logged images
DATA_DIR = os.path.join(PARENT_DIR, "tests", "data")
MAT_FILE = os.path.join(DATA_DIR, 'test_data.mat')

# Test functionality of data loaders and utilities
class TestData:
    def test_extract_labels(self, records):
        assert extract_labels(records, record_len=2).shape == (2, 2)

    def test_extract_features(self, records):
        assert extract_features(records, record_len=2).shape == (2, 2, 40)

    def test_load_dataset(self):
        features, labels = load_dataset(MAT_FILE)

        # check features
        assert isinstance(features, np.ndarray) 
        assert features.shape == (2, 2, 40)

        # check labels 
        assert isinstance(labels, np.ndarray)
        assert labels.shape == (2, 2)

        