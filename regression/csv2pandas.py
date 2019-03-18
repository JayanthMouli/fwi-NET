#convert csv to pandas dataframe without column error (delimeter confusion)
import csv
import datetime
import numpy as np
import os
from netCDF4 import Dataset
import pandas


#initialize tuples
fsize = ()
dc = ()
dmc = ()
ffmc = ()
isi = ()
bui = ()
fwi = ()

#open file
with open("fwi2015fires.csv", "r") as csvinput:
	reader = csv.reader(csvinput)
	reader.next()
	#add values to tuples
	for row in reader:
		fsize = fsize + (row[0],)
		dc = dc + (row[1],)
		dmc = dmc + (str(row[2]),)
		ffmc = ffmc + (row[3],)
		isi = isi + (row[4],)
		bui = bui + (row[5],)
		fwi = fwi + (row[6],)
#create dataframe, export as corrected csv without column error	
raw_data = { 'FIRE_SIZE':fsize,'DC':dc, 'DMC':dmc, 'FFMC':ffmc,'ISI':isi,'BUI':bui, 'FWI':fwi}
DF = pandas.DataFrame(raw_data, columns = ['FIRE_SIZE', 'DC', 'DMC', 'FFMC', 'ISI', 'BUI', 'FWI'])
DF.to_csv('fwi2015firespropcols.csv')
