import csv

with open("aptcolumns2015.csv", "r") as csvinput:
	reader = csv.reader(csvinput)
	for row in reader:
		print type(row[8])
