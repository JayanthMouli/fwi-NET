import csv

with open("out.csv", "rb") as f:
	reader = csv.reader(f)
	i = reader.next()
	print i
