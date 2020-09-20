"""import csv

def get_data_from_csv():
    dico_format = {
            "Index" : 0,
            "Hogwarts House": "house_name",
            "First Name": "first_name",
            "Last Name": "last_name",
            "Birthday": "birthday",
            "Best Hand": "hand",
            "Arithmancy": 0.0,
            "Astronomy": 0.0,
            "Herbology": 0.0,
            "Defense Against the Dark Arts": 0.0,
            "Divination": 0.0,
            "Muggle Studies": 0.0,
            "Ancient Runes": 0.0,
            "History of Magic": 0.0,
            "Transfiguration": 0.0,
            "Potions": 0.0,
            "Care of Magical Creatures": 0.0,
            "Charms": 0.0,
            "Flying": 0.0
            }
    data = []
    with open("datasets/dataset_train.csv", "r+") as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        i = 0
        for row in reader:
            data.append(fill_dico_for_student(row, dico_format))
    return data

def print_data_infos(data):
    features = list(data[0])
    print(f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
    for i in range(len(features) - 1):
        print(f'{features[i]:8.8}', end=' |')

def cast_infos_from_list(row):
    infos = ""
    for elem in row:
        infos += elem + ','
    return infos

def fill_dico_for_student(row, dico_format):
    infos = cast_infos_from_list(row)
    infos = infos.split(',')
    dico = dico_format
    dico['Index'] = infos[0]
    dico['Hogwarts House'] = infos[1]
    dico['First Name'] = infos[2]
    dico['Last Name'] = infos[3]
    dico['Birthday'] = infos[4]
    dico['Best Hand'] = infos[5]
    dico['Arithmancy'] = infos[6]
    dico['Astronomy'] = infos[7]
    dico['Herbology'] = infos[8]
    dico['Defence Against the Dark Arts'] = infos[9]
    dico['Divination'] = infos[10]
    dico['Muggle Studies'] = infos[11]
    dico['Ancient Runes'] = infos[12]
    dico['History of Magic'] = infos[13]
    dico['Transfiguration'] = infos[14]
    dico['Potions'] = infos[15]
    dico['Care of Magical Creatures'] = infos[16]
    dico['Charms'] = infos[17]
    dico['Flying'] = infos[18]
    return dico

if __name__ == "__main__":
    data = get_data_from_csv()
    print_data_infos(data)"""
import csv
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import count_, mean_, std_, min_, percentile_, max_,

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help="input dataset")
args = parser.parse_args()

def describe(filename):
  dataset = load_csv(filename)
  features = dataset[0]
  dataset = dataset[1:, :]
  print(f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
  for i in range(0, len(features)):
    print(f'{features[i]:15.15}', end=' |')
    try:
      data = np.array(dataset[:, i], dtype=float)
      data = data[~np.isnan(data)]
      if not data.any():
        raise Exception()
      print(f'{count_(data):>12.4f}', end=' |')
      print(f'{mean_(data):>12.4f}', end=' |')
      print(f'{std_(data):>12.4f}', end=' |')
      print(f'{min_(data):>12.4f}', end=' |')
      print(f'{percentile_(data, 25):>12.4f}', end=' |')
      print(f'{percentile_(data, 50):>12.4f}', end=' |')
      print(f'{percentile_(data, 75):>12.4f}', end=' |')
      print(f'{max_(data):>12.4f}')
    except:
      print(f'{count_(dataset[:, i]):>12.4f}', end=' |')
      print(f'{"No numerical value to display":>60}')

def load_csv(filename):
  dataset = list()
  with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    try:
      for _ in reader:
        row = list()
        for value in _:
          try:
            value = float(value)
          except:
            if not value:
              value = np.nan
          row.append(value)
        dataset.append(row)
    except csv.Error as e:
      print(f'file {filename}, line {reader.line_num}: {e}')
  return np.array(dataset, dtype=object)

if __name__ == "__main__":
    describe(args.dataset)
