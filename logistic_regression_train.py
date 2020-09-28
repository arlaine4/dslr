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

def xavier_init(X):
    return np.random.randn(X.shape[1]) * np.sqrt(1 / X.shape[1])

def cost(X, y, theta):
	return ((-1 / X.shape[0]) * np.sum(y * np.log(predict(X, theta)) + (1 - y) * np.log(1 - predict(X, theta))))

def new_value_for_alpha(alpha, loop):
    return (1 / (1 + alpha * loop))

def predict(X, theta):
    z = np.dot(X, theta)
    sig = 1 / (1 + np.exp(-z))
    return sig

def calcul_thetas_house(X, y, house):
    print(y)
    alpha = 1
    costs = []
    m = float(len(X))
    y = np.array(y)
    theta = xavier_init(X)
    for loop in range(3000):
        theta = theta - alpha * (1 / m) * (np.dot((predict(X, theta) - y), X))
        costs.append(cost(X, y, theta))
        alpha = new_value_for_alpha(alpha, loop)
    x = np.arange(len(costs))
    #plt.plot(x, costs)
    #plt.title("Logistic Regression for {}".format(house))
    #plt.show()
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
    thetas = np.array(thetas)
    np.savetxt("thetas.csv", thetas.T, delimiter=",", header="Gryffindor,Slytherin,Ravenclaw,Hufflepuff", comments="")
