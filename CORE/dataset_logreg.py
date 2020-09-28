import matplotlib.pyplot as plt
import pandas as pd

def get_dataset_LogReg(dataset):
    """Extraction du dataset et suppression elements useless"""
    dataset = pd.read_csv(dataset)
    dataset = dataset.fillna(0) ## change the mean dataset.fillna(dataset.mean())
    y = dataset['Hogwarts House']
    dataset = dataset[dataset.columns[6:19]]
    dataset = dataset.drop('Astronomy', axis=1)
    dataset = dataset.drop('Defense Against the Dark Arts', axis=1)
    dataset = dataset.drop('Arithmancy', axis=1)
    dataset = dataset.drop('Care of Magical Creatures', axis=1)
    dataset = dataset.drop('Potions', axis=1)
    return dataset, y

def get_theta_from_csv():
    """extraction des thetas depuis le fichier csv"""
    thetas = pd.read_csv("thetas.csv")
    theta_g = thetas['Gryffindor']
    theta_s = thetas['Slytherin']
    theta_r = thetas['Ravenclaw']
    theta_h = thetas['Hufflepuff']
    return theta_g, theta_s, theta_r, theta_h

def print_plot_houses_LogReg(x, costs, house):
    """Affichage des regression logistique"""
    plt.plot(x, costs)
    plt.title("Logistic Regression for {}".format(house))
    plt.show()
