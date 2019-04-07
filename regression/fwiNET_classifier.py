import numpy as np
import pandas
from keras.layers import Dense, Activation
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

dataframe = pandas.read_csv("fwinormalizedwithclass.csv").dropna()#.astype(np.float32)
dataset = dataframe.values
X = dataset[:,2:7]
y = dataset[:,8] #FIRE_SIZE_CLASS
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.08, random_state = 0)
regressor = RandomForestClassifier(n_estimators=20, random_state=0)  
regressor.fit(X_train, y_train)  
y_pred = regressor.predict(X_test)
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  
print(accuracy_score(y_test, y_pred))  
finalpred = regressor.predict(X)
n1 = 0
n2 = 0
for x in range(0,6000):
	if finalpred[x] == y[x]:
		n1 = n1 + 1
	else:
		n2 = n2 + 1
		
s = 'accuracy = ' + str(n1) + '/' + str(n1+n2)
plt.bar(['Correct Classification','Incorrect Classification'], [n1, n2])
plt.title('Random Forest Classification Results')
plt.text(0.5, 100, s , fontsize=12)
plt.show()
# plt.plot(y_test, color = 'red', label = 'Real data')
# plt.plot(y_pred, color = 'blue', label = 'Predicted data')
# plt.title('Prediction')
# plt.legend()