import csv
import datetime
import numpy as np
import os
from netCDF4 import Dataset
import pandas

with open("fwi2015fires.csv", "r") as csvinput:
	reader = csv.reader(csvinput)
	reader.next()
	for row in reader:
		print row[2]