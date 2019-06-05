#Using the cancer dataset with Logistic Regression

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split as tts

cancer = load_breast_cancer()

xTrain, xTest, yTrain, yTest = tts(cancer.data, cancer.target, stratify=cancer.target, random_state=42)

logreg = LogisticRegression().fit(xTrain, yTrain)
print("Training score: {:.3f}".format(logreg.score(xTest, yTest)))
print("Testing score: : {:.3f}".format(logreg.score(xTrain, yTrain)))