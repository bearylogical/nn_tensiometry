import numpy as np
import os
from typing import NewType, Sequence, Tuple

FeatureArray = NewType('FeatureArray', np.ndarray)
Features = Sequence[FeatureArray]
Labels = Sequence[np.ndarray]

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Current file marks the root directory
PARENT_DIR = os.path.dirname(ROOT_DIR)  # Directory for storing logged images
DATA_DIR = os.path.join(PARENT_DIR, "data")


def extract_txt(file:str):
    return np.loadtxt(file,  dtype="float32", delimiter=',')

def extract_labels(idx_file):
    return np.loadtxt(idx_file, skiprows=1, usecols=(0,1), delimiter=",")

def load_dataset(data_dir:str, index_file:str)->Tuple[Features, Labels]:

    data_files = [file for file in os.listdir(data_dir) if file.split('.')[-1] == "txt"]
    sorted_files = sorted(data_files, key=lambda x : int(x.split('.')[0]))

    if os.path.exists(index_file):
        labels = extract_labels(index_file)
    else:
        raise FileNotFoundError(f'{index_file} does not exist!')
    
    txt_files = []
    for file in sorted_files:
        fp = os.path.join(data_dir, file)
        txt_files.append(fp)
    
    features = np.asarray([extract_txt(f) for f in txt_files])

    if features is None:
        raise ValueError('No features for input!')
    
    return features, labels

    
if __name__ == "__main__":
    index_file_path = os.path.join(DATA_DIR, "index.csv")
    load_dataset(DATA_DIR, index_file_path)