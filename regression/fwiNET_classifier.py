#fwiNET main program
#created by Jayanth Mouli 2019

###########################################################################################################################################
import numpy as np
import pandas
from keras.layers import Dense, Activation
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#read data
dataframe = pandas.read_csv("fwinormalizedwithclass.csv").dropna()#.astype(np.float32)
dataset = dataframe.values
X = dataset[:,2:7]
y = dataset[:,8] #FIRE_SIZE_CLASS

#split train, test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.08, random_state = 0)

#initialize regressor as RF classifier
regressor = RandomForestClassifier(n_estimators=20, random_state=0) 

#train regressor
regressor.fit(X_train, y_train)  

#predict test array
y_pred = regressor.predict(X_test)

#print accuracy metrics
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  
print(accuracy_score(y_test, y_pred)) 

#predict test array
finalpred = regressor.predict(X)

n1 = 0
n2 = 0
for x in range(0,6000): #test the first 6000  elements of the data (total data is near 6000)
	if finalpred[x] == y[x]: #prediction is correct
		n1 = n1 + 1
	else:      #prediction is incorrect
		n2 = n2 + 1
		
#concatonate string		
s = 'accuracy = ' + str(n1) + '/' + str(n1+n2)

#plot results as bar graph
plt.bar(['Correct Classification','Incorrect Classification'], [n1, n2])
plt.title('Random Forest Classification Results')
plt.text(0.5, 100, s , fontsize=12)
plt.show()
# plt.plot(y_test, color = 'red', label = 'Real data')
# plt.plot(y_pred, color = 'blue', label = 'Predicted data')
# plt.title('Prediction')
# plt.legend()
