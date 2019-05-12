#Ridge Regression

#RR is a form of linear regression but allows you to modify it more

"""
In  ridge  regression,though, the coefficients (w) are chosen not only so that they predict well on the 
train‐ing data, but also to fit an additional constraint. We also want the magnitude of coef‐ficients  to  be  as  
small  as  possible;  in  other  words,  all  entries  of  w  should  be  close  tozero. Intuitively, this means 
each feature should have as little effect on the outcome aspossible  (which  translates  to  having  a  small  slope),
while  still  predicting  well.  Thisconstraint is an example of what is called regularization. 
  
Regularization means explicitly restricting a model to avoid overfitting. 
The particular kind used by ridge regression is known as L2 regularization.
"""

import mglearn
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

x, y = mglearn.datasets.load_extended_boston()
xTrain, xTest, yTrain, yTest = tts(x, y, random_state=0)



"""
The  Ridge  model  makes  a  trade-off  between  the  simplicity  of  the  model  (near-zerocoefficients)  
and  its  performance  on  the  training  set.  How  much  importance  themodel  places  on  simplicity  versus  
training  set  performance  can  be  specified  by  theuser, using the alpha parameter. 
In the previous example, we used the default param‐eter  alpha=1.0.  
There  is  no  reason  why  this  will  give  us  the  best  trade-off,  though.The  optimum  setting  of  alpha  
depends  on  the  particular  dataset  we  are  using.

Increasing  alpha  forces  coefficients  to  move  more  toward  zero,  
which  decreasestraining set performance but might help generalization. 
"""

neigh_settings = range(0, 10)

trainAcc = []
testAcc = []

for n in neigh_settings:
    ridge = Ridge(alpha=n*.1).fit(xTrain, yTrain)

    trainAcc.append(ridge.score(xTrain, yTrain))
    
    testAcc.append(ridge.score(xTest, yTest))
    

print("Training: {:.2f}".format(ridge.score(xTrain, yTrain)))
print("Testing: {:.2f}".format(ridge.score(xTest, yTest)))


plt.plot(neigh_settings, trainAcc, label="training accuracy")
plt.plot(neigh_settings, testAcc, label="testing accuracy")
plt.ylabel("Accuracy")
plt.xlabel("CoeffSize (*10)")

plt.legend()