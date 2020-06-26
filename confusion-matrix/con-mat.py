from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
actual=[1,1,1,0,0,1,1,0,1,0]
predic=[0,1,0,1,0,1,1,1,1,0]
print(confusion_matrix(actual,predic))
print(" ")
print(accuracy_score(actual,predic))
print(classification_report(actual,predic))

