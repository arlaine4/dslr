import describe
import numpy as np
import argparse
from CORE.core_graphs import print_histogram

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help='input dataset')
option = parser.parse_args()

if __name__ == "__main__":
    data = describe.load_csv(option.dataset)
    data = data[1:, :]
    data = data[data[:, 1].argsort()]
    data = np.array(data[:, 16], dtype=float)
    legend = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    print_histogram(data, legend, "Marks", "Number of students")
