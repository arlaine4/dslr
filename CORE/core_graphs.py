import numpy as np
import CORE.maths
import argparse
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

def pair_plot(dataset):
    sns.set(style="ticks", color_codes=True)
    dataset.dropna(inplace=True)
    dataset = dataset.drop('Astronomy', axis='columns')
    dataset = dataset.drop('Defense Against the Dark Arts', axis='columns')
    sns.pairplot(dataset, hue = 'Hogwarts House', height=1)
    plt.show()

def get_house_grades(dataset, gradedata, house, grade):
    data = gradedata[dataset["Hogwarts House"] == house][grade]
    data = data.copy()
    data.dropna(inplace=True)
    return data

def print_histogram(data, gradedata):
    for c in gradedata.columns:
        plt.figure()
        plt.hist(get_house_grades(data, gradedata, "Gryffindor", c), bins=50, label="Gryffindor", color='r', alpha=0.5)
        plt.hist(get_house_grades(data, gradedata, "Slytherin", c), bins=50, label="Slytherin", color='g', alpha=0.5)
        plt.hist(get_house_grades(data, gradedata, "HUfflepuff", c), bins=50, label="Hufflepuff", color='b', alpha=0.5)
        plt.hist(get_house_grades(data, gradedata, "Ravenclaw", c), bins=50, label="Ravenclaw", color='y', alpha=0.5)
        plt.title(c)
        plt.legend(loc='upper right')
        plt.show()
        
def scatter_plot(x, y, legend, x_label, y_label):
    plt.scatter(x[:327], y[:327], color='red', alpha=0.5)
    plt.scatter(x[327:856], y[327:856], color='yellow', alpha=0.5)
    plt.scatter(x[856:1299], y[856:1299], color='blue', alpha=0.5)
    plt.scatter(x[1299:], y[1299:], color='green', alpha=0.5)
    plt.legend(legend, loc='upper right', frameon=True)
    plt.title("Similar features")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
