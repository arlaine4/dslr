import numpy as np
import pandas as pd
import argparse
from CORE.core_graphs import print_histogram

#-----------------------------------------------------------------
# Initialisation du parseur d'arguments

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help='input dataset')
options = parser.parse_args()

#
#-----------------------------------------------------------------

if __name__ == "__main__":
    #-----------------------------------------------------------------
    # Preparation de la data

    dataset = pd.read_csv(options.dataset)
    gradedata = dataset[dataset.columns[6:19]]
    #
    #-----------------------------------------------------------------
    print_histogram(dataset, dataset[gradedata.columns.values])
