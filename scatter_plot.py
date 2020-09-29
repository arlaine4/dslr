import csv
import argparse
import numpy as np
import describe
import matplotlib.pyplot as plt
from CORE.core_graphs import scatter_plot

#----------------------------------------------------------------------
# Initialisation du parseur d'arguments

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help="input dataset")
options = parser.parse_args()

#
#----------------------------------------------------------------------

if __name__ == "__main__":
    #----------------------------------------------------------------------
    # Preparation de la data

    dataset = describe.load_csv(options.dataset)
    data = dataset[1:, :]
    data = data[data[:, 1].argsort()]
    X = np.array(data[:, 7], dtype=float)
    y = np.array(data[:, 9], dtype=float)
    legend = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    #
    #----------------------------------------------------------------------
    scatter_plot(X, y, legend, dataset[0, 7], dataset[0, 9]) 
