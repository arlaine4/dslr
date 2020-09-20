import describe
import numpy as np
import maths
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help='input dataset')
option = parser.parse_args()

def print_histogram(data):
    for i in range(5):
        data.delete(data[i], i)
    gryffindor = data[:maths.percentile_(data, 25)]
    hufflepuff = data[maths.percentile_(data, 25):maths.percentile_(data, 50)]
    ravenclaw = data[maths.percentile_(data, 50):maths.percentile_(data, 75)]
    slytherin = data[maths.percentile_(data, 75):]
    pass 

if __name__ == "__main__":
    data = describe.load_csv(option.dataset)
    data = data[1:, :]
    data = data[data[:, 1].argsort()]
    for i in range(len(data)):
        if i % 10 == 0:
            print(data[i])
    print_histogram(data)
