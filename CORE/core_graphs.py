import numpy as np
import CORE.maths
import argparse
import matplotlib.pyplot as plt
import matplotlib

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

def pair_plot(dataset, features, legend):
    font = {'family' : 'DejaVu Sans',
                'weight' : 'light',
                'size'   : 7}
    matplotlib.rc('font', **font)

    size = dataset.shape[1]
    _, ax = plt.subplots(nrows=size, ncols=size)
    plt.subplots_adjust(wspace=0.15, hspace=0.15)
    for row in range(0, size):
        for col in range(0, size):
            X = dataset[:, col]
            y = dataset[:, row]
            if col == row:
                pair_plot_hist(ax[row, col], X)
            else:
                pair_plot_scatter(ax[row, col], X, y)
            if ax[row, col].is_last_row():
                ax[row, col].set_xlabel(features[col].replace(' ', '\n'))
            else:
                ax[row, col].tick_params(labelbottom=False)
            if ax[row, col].is_first_col():
                ax[row, col].set_ylabel(features[row].replace(' ', '\n'))
            else:
                ax[row, col].tick_params(labelleft=False)
        ax[row, col].spines['right'].set_visible(False)
        ax[row, col].spines['top'].set_visible(False)
    plt.legend(legend, loc='center left', frameon=False, bbox_to_anchor=(1, 0.5))
    plt.show()

def pair_plot_hist(ax, X):
    h1 = X[:327]
    h1 = h1[~np.isnan(h1)]
    ax.hist(h1, alpha=0.5)
    h2 = X[327:856]
    h2 = h2[~np.isnan(h2)]
    ax.hist(h2, alpha=0.5)
    h3 = X[856:1299]
    h3 = h3[~np.isnan(h3)]
    ax.hist(h3, alpha=0.5)
    h4 = X[1299:]
    h4 = h4[~np.isnan(h4)]
    ax.hist(h4, alpha=0.5)

def pair_plot_scatter(ax, X, y):
    ax.scatter(X[:327], y[:327], s=1, color='red', alpha=0.5)
    ax.scatter(X[327:856], y[327:856], s=1, color='yellow', alpha=0.5)
    ax.scatter(X[856:1299], y[856:1299], s=1, color='blue', alpha=0.5)
    ax.scatter(X[1299:], y[1299:], s=1, color='green', alpha=0.5)
