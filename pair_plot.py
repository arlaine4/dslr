import argparse
import numpy as np
import matplotlib.pyplot as plt
from CORE.core_graphs import pair_plot
from describe import load_csv

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help="input dataset")
options = parser.parse_args()

if __name__ == "__main__":
    dataset = load_csv(options.dataset)
    data = dataset[1:, 6:]
    data = data[data[:, 1].argsort()]

    features = dataset[0, 6:]
    legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    pair_plot(np.array(data, dtype=float), features, legend)
