#Lasso Linear Model
"""
An  alternative  to  Ridge  for  regularizing  linear  regression  is  Lasso.  
As  with  ridge regression,  using  the  lasso  also  restricts  coefficients  to  be  close  to  zero,  
but  in  aslightly different way, called L1 regularization.

The consequence of L1 regularization is that when using the lasso, some coefficients are exactly zero. 
This means some features are entirely ignored by the model.
 
This can be seen as a form of automatic feature selection. 

Having some coefficients be exactly zero often makes a model easier tointerpret, 
and can reveal the most important features of your model.
"""

import mglearn
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

x, y = mglearn.datasets.load_extended_boston()

xTrain, xTest, yTrain, yTest = tts(x, y, random_state=0)

lasso = Lasso().fit(xTrain, yTrain)

print("Training Score: {:.2f}".format(lasso.score(xTrain, yTrain)))
print("Testing Score: {:.2f}".format(lasso.score(xTest, yTest)))
print("Number of features used: {}".format(np.sum(lasso.coef_ != 0)))

print()

#29
#20
#We are underfitting, and quite awfully

lassoTwo = Lasso(alpha=0.01, max_iter=100000).fit(xTrain, yTrain)

print("Neu Training Score: {:.2f}".format(lassoTwo.score(xTrain, yTrain)))
print("Neu Testing Score: {:.2f}".format(lassoTwo.score(xTest, yTest)))
print("Number of features used: {}".format(np.sum(lassoTwo.coef_ != 0)))

"""This is much better"""