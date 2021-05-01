import matplotlib.pyplot as plt
import numpy as np

def plot_image(data_array, label):
    img = np.reshape(np.ravel(data_array), (2,207),'F')
    plt.figure()
    