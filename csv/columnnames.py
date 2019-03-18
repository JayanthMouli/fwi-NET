#convenience file to get column names from initial raw csv post sqlite convert

import csv

with open("out.csv", "rb") as f:
	reader = csv.reader(f)
	i = reader.next()
	print i
