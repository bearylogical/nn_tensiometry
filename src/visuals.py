import matplotlib.pyplot as plt
import numpy as np

def plot_image(ax, data_array, label_array):
    ax.plot(data_array[0], data_array[1])
    ax.set_xlim(left=0)
    ax.set_ylim(top=0)
    ax.set_xlabel('r')
    ax.set_ylabel('z')
    ax.text(0.01, 0, f'$\sigma_0 = {label_array[0]:.3f}$ , Vol0 = {label_array[1]:.3f}', fontsize=8, verticalalignment='top',)
    return ax