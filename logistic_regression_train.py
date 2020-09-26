import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help="input dataset")
options = parser.parse_args()

def StandardScaler(X):
    mean = np.mean(X, axis=0)
    scale = np.std(X - mean, axis=0)
    return (X - mean) / scale

def rework_dataset(dataset):
    """Function that gets rid of 'useless' data and returns a 'clean' dataset"""
    dataset = dataset.fillna(dataset.mean())
    y = dataset['Hogwarts House']
    dataset = dataset[dataset.columns[6:19]]
    dataset = dataset.drop('Astronomy', axis=1)
    dataset = dataset.drop('Defense Against the Dark Arts', axis=1)
    dataset = dataset.drop('Arithmancy', axis=1)
    dataset = dataset.drop('Care of Magical Creatures', axis=1)
    dataset = dataset.drop('Potions', axis=1)
    return dataset, y

def calcul_thetas_house(X, y, house):
    alpha = 1
    m = float(len(X))
    y = np.array(y)
    print(y)
    theta = X
    return theta

def Logistic_Regression(X, y):
    y_g = y.replace({"Gryffindor" : 1, "Slytherin" : 0, "Ravenclaw" : 0, "Hufflepuff" : 0})
    y_s = y.replace({"Gryffindor" : 0, "Slytherin" : 1, "Ravenclaw" : 0, "Hufflepuff" : 0})
    y_r = y.replace({"Gryffindor" : 0, "Slytherin" : 0, "Ravenclaw" : 1, "Hufflepuff" : 0})
    y_h = y.replace({"Gryffindor" : 0, "Slytherin" : 0, "Ravenclaw" : 0, "Hufflepuff" : 1})
    t_g = calcul_thetas_house(X, y_g, "Gryffindor")
    t_s = calcul_thetas_house(X, y_s, "Slytherin")
    t_r = calcul_thetas_house(X, y_r, "Ravenclaw")
    t_h = calcul_thetas_house(X, y_h, "Hufflepuff")
    thetas = [t_g, t_s, t_r, t_h]
    return thetas

if __name__ == "__main__":
    dataset = pd.read_csv(options.dataset)
    dataset, y = rework_dataset(dataset)
    X = np.array(dataset)
    X = StandardScaler(X)
    X = np.c_[np.ones(X.shape[0]), X]
    thetas = Logistic_Regression(X, y)
    #print(X)

