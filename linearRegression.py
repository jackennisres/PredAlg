#Linear regression
"""
Linear regression, or ordinary least squares (OLS), is the simplest and most classic linear method for regression. 
Linear regression finds the parameters w and b that mini‐mize  
the  mean  squared  error  between  predictions  and  the  true  regression  targets, y, 
on  the  training  set.  

The  mean  squared  error  is  the  sum  of  the  squared  differencesbetween the predictions and the true values, 
divided by the number of samples. Lin‐ear regression has no parameters, which is a benefit, but it also has no way 
to control model complexity.
"""


import mglearn
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression


x, y = mglearn.datasets.make_wave(n_samples=60)
xTrain, xTest, yTrain, yTest = tts(x, y, random_state=42)

lr = LinearRegression().fit(xTrain, yTrain)

"""
The “slope” parameters (w), also called weights or coefficients, are stored in the coef_attribute, 
while the offset or intercept (b) is stored in the intercept_ attribute:
"""

print("lr.coef_: {}".format(lr.coef_))
print("lr.intercept_: {}".format(lr.intercept_))

print()

print("Training set score: {}".format(lr.score(xTrain, yTrain)))
print("Testing set score: {}".format(lr.score(xTest, yTest)))