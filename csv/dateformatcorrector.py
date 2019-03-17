import csv
import datetime

def convert(default):
	special = default[5:7]+ default[8:10]
	print special
if __name__=='__main__':
	convert('2015-07-09')
