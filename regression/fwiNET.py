#fwiNET multilayer perceptron regressor
#created by Jayanth Mouli 2019

###########################################################################################################################################
import numpy as np
import pandas
from keras.layers import Dense, Activation
from keras.models import Sequential
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# Importing the dataset
dataframe = pandas.read_csv("fwi2015firesnormalized.csv").dropna().astype(np.float32)
dataset = dataframe.values
X = dataset[:,2:]
y = dataset[:,1]

# correlation = dataframe['FWI'].corr(dataframe['FIRE_SIZE'])
# print correlation
# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.008, random_state = 0)

# Initialising the ANN
model = Sequential()

# Adding the input layer and the first hidden layer
model.add(Dense(32, activation = 'relu', input_dim = 6))

# Adding the second hidden layer
model.add(Dense(units = 32, activation = 'relu'))

# Adding the third hidden layer
model.add(Dense(units = 32, activation = 'relu'))

# Adding the output layer

model.add(Dense(units = 1))

#model.add(Dense(1)) does the same thing
# Compiling the ANN
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the ANN to the Training set
model.fit(X_train, y_train, batch_size = 128, epochs = 500)

y_pred = model.predict(X_test)

plt.plot(y_test, color = 'red', label = 'Real data')
plt.plot(y_pred, color = 'blue', label = 'Predicted data')
plt.title('Prediction')
plt.legend()
plt.savefig('traintest1.png')
plt.show()

