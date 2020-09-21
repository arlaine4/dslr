import numpy as np
import CORE.maths
import argparse
import matplotlib.pyplot as plt

def print_histogram(data, legend, x_label, y_label):
    gryffindor = data[:327]
    gryffindor = gryffindor[~np.isnan(gryffindor)]
    plt.hist(gryffindor, color='red', alpha=0.5)
    hufflepuff = data[327:856]
    hufflepuff = hufflepuff[~np.isnan(hufflepuff)]
    plt.hist(hufflepuff, color='yellow', alpha=0.5)
    ravenclaw = data[856:1299]
    ravenclaw = ravenclaw[~np.isnan(ravenclaw)]
    plt.hist(ravenclaw, color='blue', alpha=0.4)
    slytherin = data[1299:]
    slytherin = slytherin[~np.isnan(slytherin)]
    plt.hist(slytherin, color='green', alpha=0.3)

    plt.legend(legend, loc='upper right', frameon=True)
    plt.title("Grades scale for Poudlard's houses")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def scatter_plot(x, y, legend, x_label, y_label):
    plt.scatter(x[:327], y[:327], color='red', alpha=0.5)
    plt.scatter(x[327:856], y[327:856], color='yellow', alpha=0.5)
    plt.scatter(x[856:1299], y[856:1299], color='blue', alpha=0.5)
    plt.scatter(x[1299:], y[1299:], color='green', alpha=0.5)
    plt.legend(legend, loc='upper right', frameon=True)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
