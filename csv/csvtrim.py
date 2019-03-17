import csv


with open("out.csv", "r") as csvinput:
	with open("revised.csv", "w") as csvoutput:
		writer = csv.writer(csvoutput)
		reader = csv.reader(csvinput)
		d_reader = csv.DictReader(csvinput)
		headers = d_reader.fieldnames
		writer.writerow(headers)
		for row in reader:
			if row[34] == 'CA':
				writer.writerow(row)

	
