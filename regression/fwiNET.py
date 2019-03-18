#fwiNET main program
#created by Jayanth Mouli 2019

###########################################################################################################################################
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

dataframe = pandas.read_csv("fwi2015firesnormalized.csv")
dataset = dataframe.values
X = dataset[:,1:7]
Y = dataset[:,1]

def baseline_model():
	model = Sequential()
	model.add(Dense(6, input_dim=6, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal'))
	model.compile(loss='mean_squared_error', optimizer='adam')
	history = model.fit(X, Y, epochs=1000, verbose=0)
	print history
	
if __name__ == '__main__':
	firenet = baseline_model()
	seed = 7
	numpy.random.seed(seed)
	kfold = KFold(n_splits = 10, random_state = seed)
	results = cross_val_score(firenet, X, Y, cv=kfold)
	print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))
	
