#trims initial csv file raw from sqlite conversion to relevent information for FWI calculations (precipitation, moisture, relative humidity, etc.)


import csv
import datetime
import numpy as np
import os
from netCDF4 import Dataset


def core():
	dirname = '/home/***/Desktop/fire/netcdfreader/MERRA2'


	with open("merrafires2015.csv", "r") as csvinput:
		with open("merra2015final.csv", "w") as csvoutput:
			reader = csv.reader(csvinput)
			writer = csv.writer(csvoutput)
			for row in reader:
				ary = []
				ary.append(str(row[6]))
				ary.append(str(row[11]))
				ary.append(str(row[12]))
				ary.append(str(row[13]))
				ary.append(str(row[14]))
				writer.writerow(ary)

				
if __name__=='__main__':
	core()

	
