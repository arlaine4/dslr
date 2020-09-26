import argparse
import pandas as pd
from CORE.core_graphs import pair_plot

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help="input dataset")
options = parser.parse_args()

if __name__ == "__main__":
    dataset = pd.read_csv(options.dataset)
    pair_plot(dataset) 
