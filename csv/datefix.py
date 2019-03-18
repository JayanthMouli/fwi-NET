
#creates more convenient date values that can be easily queried upon search for relevant NETCDF file

import datetime
import csv

with open("aptcolumns2015.csv", "r") as csvinput:
	with open("datefix2015.csv", "w") as csvoutput:
		reader = csv.reader(csvinput)
		writer = csv.writer(csvoutput)
		d_reader = csv.DictReader(csvinput)
		headers = d_reader.fieldnames
		newheader = 'REVISED_DATE'
		headers.append(newheader)
		writer.writerow(headers)
		for row in reader:
			ary = row
			#take initial date given, add duration of wildfire
			dt_init = datetime.date(2015, 1, 1)
			dt_delta = datetime.timedelta(int(row[3]))
			default = str(dt_init + dt_delta)
			#concatonate final convenience string that has MMDD format
			special = default[5:7]+ default[8:10]
			ary.append(special)
			writer.writerow(ary)
			
