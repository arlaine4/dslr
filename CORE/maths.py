import numpy as np

def mean_matrice_(X):
    mean_ = np.sum(X, axis=0)
    mean_ /= 1600
    mean_ = np.array(mean_)
    return mean_

def count_(X):
    try:
        X = X.astype('float')
        return len(X)
    except:
        return len(X)

def mean_(X):
    total = 0
    for x in X:
        total = total + x
    return total / len(X)

def std_(X):
    mean = mean_(X)
    total = 0
    for x in X:
        total = total + (x - mean) ** 2
    return (total / len(X)) ** 0.5

def min_(X):
    X.sort()
    min_ = X[0]
    return min_

def max_(X):
    X.sort()
    max_ = X[len(X) - 1]
    return max_

def percentile_(X, p):
    k = (len(X) - 1) * (p / 100)
    f = np.floor(k)
    c = np.ceil(k)
    if f == c:
        return X[int(k)]
    d0 = X[int(f)] * (c - k)
    d1 = X[int(c)] * (k - f)
    return d0 + d1
