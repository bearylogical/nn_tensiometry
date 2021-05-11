import numpy as np
import os
from typing import NewType, Sequence, Tuple
from scipy.io import loadmat

FeatureArray = NewType('FeatureArray', np.ndarray)
Features = Sequence[FeatureArray]
Labels = Sequence[np.ndarray]

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Current file marks the root directory
PARENT_DIR = os.path.dirname(ROOT_DIR)  # Directory for storing logged images
DATA_DIR = os.path.join(PARENT_DIR, "data")


def extract_features(records:np.ndarray, record_len:int)->np.ndarray:
    """Function extract features from Matlab struct

    Args:
        records (np.ndarray): Array of Record struct from Matlab
        record_len (int): Total number of records

    Returns:
        [np.ndarray]: Output array of shape (record_len, 2) 
    """
    r = [records['record'][i]['r'].item() for i in range(record_len)]
    z = [records['record'][i]['z'].item() for i in range(record_len)]
    return np.asarray(tuple(zip(r, z)))

def extract_labels(records:np.ndarray, record_len:int)->np.ndarray:
    """Function to extract labels (sig0, vol0) from Matlab struct

    Args:
        records (np.ndarray): Array of Record struct from Matlab
        record_len (int): Total number of records

    Returns:
        [np.ndarray]: Output array of shape (record_len, 2) 
    """
    sig0 = [records['record'][i]['sig0'].item() for i in range(record_len)]
    vol0 = [records['record'][i]['vol0'].item() for i in range(record_len)]
    return np.asarray(tuple(zip(sig0, vol0)))

def load_dataset(m_file:str)->Tuple[Features, Labels]:

    if os.path.exists(m_file):
        records = loadmat(m_file, squeeze_me=True, mat_dtype=True)['records']
        record_len = len(records)
        features = extract_features(records=records, record_len=record_len)
        labels = extract_labels(records=records, record_len=record_len)

        return features, labels
    else:
        raise FileNotFoundError(f'{m_file} does not exist!')


if __name__ == "__main__":
    m_file = os.path.join(DATA_DIR, "data.mat")
    load_dataset(m_file)