import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
from CORE.maths import mean_matrice_
from CORE.dataset_logreg import get_dataset_LogReg, print_plot_houses_LogReg


#-----------------------------------------------------------------------------------------#
# Initialisation du parseur d'arguments

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help="input dataset")
options = parser.parse_args()

#
#-----------------------------------------------------------------------------------------#

def StandardScaler(X):
    """Scaling de la data avant la regression logistique"""
<<<<<<< HEAD
=======
    #mean = mean_matrice_(X)
>>>>>>> 69689aac24bc944967299def76b914e37c9ef021
    mean = np.mean(X, axis=0)
    scale = np.std(X - mean, axis=0)
    return (X - mean) / scale

def xavier_init(X):
    """Initialisation de xavier 'random' """
    return np.random.randn(X.shape[1]) * np.sqrt(1 / X.shape[1])

def cost(X, y, theta):
    """Fonction de calcul de cout (ou loss)"""
    return ((-1 / X.shape[0]) * np.sum(y * np.log(predict(X, theta)) + (1 - y) * np.log(1 - predict(X, theta))))

def new_value_for_alpha(alpha, loop):
    """Ajustement du learning rate"""
    return (1. / (1. + alpha * loop))

def predict(X, theta):
    z = np.dot(X, theta)
    sig = 1 / (1 + np.exp(-z))
    return sig

def calcul_thetas_house(X, y, house):
    """regression logistique pour calcul des thetas de chaque maison"""
    alpha = 1           #-------> alpha = learning_rate
    costs = []          #-------> liste des couts a chaque tour
    m = float(len(X))   #-------> m = taille echantillon
    y = np.array(y)
    theta = xavier_init(X)
    for loop in range(3000):
        theta = theta - alpha * (1 / m) * (np.dot((predict(X, theta) - y), X))
        costs.append(cost(X, y, theta))
        alpha = new_value_for_alpha(alpha, loop)
    x = np.arange(len(costs))
    #print_plot_houses_LogReg(x, costs, house)
    return theta

def Logistic_Regression(X, y):
    #-----------------------------------------------------------------------------------------#
    # Preparation et calcul des weights pour chaque maison
    y_g = y.replace({"Gryffindor" : 1, "Slytherin" : 0, "Ravenclaw" : 0, "Hufflepuff" : 0})
    y_s = y.replace({"Gryffindor" : 0, "Slytherin" : 1, "Ravenclaw" : 0, "Hufflepuff" : 0})
    y_r = y.replace({"Gryffindor" : 0, "Slytherin" : 0, "Ravenclaw" : 1, "Hufflepuff" : 0})
    y_h = y.replace({"Gryffindor" : 0, "Slytherin" : 0, "Ravenclaw" : 0, "Hufflepuff" : 1})
    t_g = calcul_thetas_house(X, y_g, "Gryffindor")
    t_s = calcul_thetas_house(X, y_s, "Slytherin")
    t_r = calcul_thetas_house(X, y_r, "Ravenclaw")
    t_h = calcul_thetas_house(X, y_h, "Hufflepuff")
    #
    #-----------------------------------------------------------------------------------------#
    thetas = [t_g, t_s, t_r, t_h]
    return thetas

if __name__ == "__main__":
    #-----------------------------------------------------------------------------------------#
    # Extraction et preparation de la data
    dataset, y = get_dataset_LogReg(options.dataset)
    X = np.array(dataset)
    X = StandardScaler(X)
    X = np.c_[np.ones(X.shape[0]), X]
    #
    #-----------------------------------------------------------------------------------------#
    thetas = Logistic_Regression(X, y)
    thetas = np.array(thetas)
    np.savetxt("thetas.csv", thetas.T, delimiter=",", header="Gryffindor,Slytherin,Ravenclaw,Hufflepuff", comments="")
