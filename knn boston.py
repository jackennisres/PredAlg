#Nearest Neighbor Boston

###my attempt at nearest neighbor for the boston dataset

import mglearn
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as KNC

boston = mglearn.datasets.load_extended_boston

xTrain, yTrain, xTest, yTest = tts(boston['data'], boston['target'])
#print(xTrain)