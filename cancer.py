from sklearn.datasets import load_breast_cancer as lbc
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as knc


cancer = lbc()
xTrain, xTest, yTrain, yTest = tts(cancer['data'], cancer['target'], stratify=cancer['target'], random_state=66)

training_acc = []
test_acc = []

#try n neighbors from 1-10
neighbors_settings = range(1,10)

for n_neighbors in neighbors_settings:
    #now we build the model
    
    print("isReached3")  
    
    clf = knc(n_neighbors=n_neighbors)
    
    print("isReached2")  
    
    clf.fit(xTrain, yTrain)
    
    print("isReached1")  
    
    #Now that we've created the fit line - we want to record the TRAINING accuracy in our list
    training_acc.append(clf.score(xTrain, yTrain))
    
    print("isReached0")    
    
    #Now we want to record the TESTING accuracy of our clf
    test_acc.append(clf.score(xTest, yTest))
    
plt.plot(neighbors_settings, training_acc, label="training accuracy")
plt.plot(neighbors_settings, test_acc, label="testing accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")

plt.legend()
    