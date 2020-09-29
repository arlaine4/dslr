import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse
from CORE.dataset_logreg import get_dataset_LogReg, get_theta_from_csv
from logistic_regression_train import StandardScaler


#-----------------------------------------------------------------------------------#
# Initalisation du parseur d'arguments

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help="input dataset for prediction")
options = parser.parse_args()

#
#-----------------------------------------------------------------------------------#

def predict(X, theta):
    z = np.dot(X, theta)
    sig = 1 / (1 + np.exp(-z))
    return sig

if __name__ == "__main__":
    #--------------------------------------------------------------#
    # Extraction et preparation de la data
    dataset, y = get_dataset_LogReg(options.dataset)
    X = np.array(dataset)
    X = StandardScaler(X)
    X = np.c_[np.ones(X.shape[0]), X]
    theta_g, theta_s, theta_r, theta_h = get_theta_from_csv()
    #
    #--------------------------------------------------------------#
    prediction = []
    pred_g = predict(X, theta_g)
    pred_s = predict(X, theta_s)
    pred_r = predict(X, theta_r)
    pred_h = predict(X, theta_h)
    for i in range(len(pred_g)):
        grade = 0
        house = 0
        if pred_g[i] > pred_s[i]:
            grade = pred_g[i]
            house = 'Gryffindor'
        else:
            grade = pred_s[i]
            house = 'Slytherin'
        if pred_r[i] > grade:
            grade = pred_r[i]
            house = 'Ravenclaw'
        if pred_h[i] > grade:
            grade = pred_h[i]
            house = 'Hufflepuff'
        prediction.append(house)
    prediction = np.array(prediction)
    prediction = pd.DataFrame(prediction, columns=['Hogwarts House'])
    prediction = prediction.rename_axis('Index', axis=0)
    prediction.to_csv('houses.csv')
