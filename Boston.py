#Boston Housing Dataset

import mglearn
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression

x, y = mglearn.datasets.load_extended_boston()
xTrain, xTest, yTrain, yTest = tts(x, y, random_state=0)
lr = LinearRegression().fit(xTrain, yTrain)

print("Training Score: {:.2f}".format(lr.score(xTrain, yTrain)))
print("Test Score: {:.2f}".format(lr.score(xTest, yTest)))

###For this dataset, we can see that the:
#Training Score: 95%
#Testing Score: 61%

#What is the deal with the test score being so low? This is a sign of overfitting
#and we need to use a different model to solve this problem
