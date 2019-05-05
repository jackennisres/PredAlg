import pandas as pd
import numpy as np
import mglearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as knc


iri = load_iris()

xTrain, xTest, yTrain, yTest = train_test_split(iri['data'], iri['target'], random_state=0)

print(xTrain.shape)

print(iriFrame)

iriFrame = pd.DataFrame(xTrain, columns=iri.feature_names)
knn = knc(n_neighbors=1)
knn.fit(xTrain, yTrain)

prediction = knn.predict(np.array([[.1, .1, .1, 0.2]]))
print(prediction)
print(iri['target_names'][prediction])

yPred = knn.predict(xTest)
print("Test predictions {}".format(yPred))
print('Test set score {:.2f}'.format(np.mean(yPred == yTest)))
#pd.plotting.scatter_matrix(iriFrame, c=yTrain, figsize=(15, 15), marker='o', hist_kwds={'bins':20}, s=60, alpha=.8, cmap=mglearn.cm3)



#print('Keys: \n{}'.format(iri.keys()))
#print(iri['data'])
#print(iri['feature_names'])
