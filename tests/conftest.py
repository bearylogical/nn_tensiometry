import pytest
import os
from scipy.io import loadmat

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Current file marks the root directory
PARENT_DIR = os.path.dirname(ROOT_DIR)  # Directory for storing logged images
DATA_DIR = os.path.join(PARENT_DIR, "tests", "data")
MAT_FILE = os.path.join(DATA_DIR, 'test_data.mat')

@pytest.fixture
def records():
    return loadmat(MAT_FILE, squeeze_me=True, mat_dtype=True)['records']
