import csv
import datetime
import numpy as np
import os
from netCDF4 import Dataset
import pandas


fsize = []
dc = []
dmc = []
ffmc = []
isi = []
bui = []
fwi = []

fsizenorm = []
dcnorm = []
dmcnorm = []
ffmcnorm = []
isinorm = []
buinorm = []
fwinorm = []
with open('fwi2015firespropcols.csv', 'r') as csvinput:
	reader = csv.reader(csvinput)
	reader.next()
	for row in reader:
		fsize.append(float(row[0]))
		dc.append(float(row[1]))
		dmc.append(float(row[2]))
		ffmc.append(float(row[3]))
		isi.append(float(row[4]))
		bui.append(float(row[5]))
		fwi.append(float(row[6]))
	
MAX_fsize = max(fsize)
MAX_dc = max(dc)
MAX_dmc = max(dmc)
MAX_ffmc = max(ffmc)
MAX_isi = max(isi)
MAX_bui = max(bui)
MAX_fwi = max(fwi)

MIN_fsize = min(fsize)
MIN_dc = min(dc)
MIN_dmc = min(dmc)
MIN_ffmc = min(ffmc)
MIN_isi = min(isi)
MIN_bui = min(bui)
MIN_fwi = min(fwi)

for F_S in range(0, len(fsize)):
	fsizenorm.append(((fsize[F_S] - MIN_fsize) / (MAX_fsize - MIN_fsize)))
for d in range(0, len(dc)):
	dcnorm.append(((dc[d] - MIN_dc) / (MAX_dc - MIN_dc)))
for dm in range(0, len(dmc)):
	dmcnorm.append(((dmc[dm] - MIN_dc) / (MAX_dmc- MIN_dmc)))
for ff in range(0, len(ffmc)):
	ffmcnorm.append(((ffmc[ff] - MIN_ffmc) / (MAX_ffmc - MIN_ffmc)))
for i in range(0, len(isi)):
	isinorm.append(((isi[i] - MIN_isi) / (MAX_isi - MIN_isi)))
for b in range(0, len(bui)):
	buinorm.append(((bui[b] - MIN_bui) / (MAX_bui - MIN_bui)))
for fw in range(0, len(fwi)):
	fwinorm.append(((fwi[fw] - MIN_fwi) / (MAX_fwi - MIN_fwi)))

raw_data = { 'FIRE_SIZE':fsizenorm,'DC':dcnorm, 'DMC':dmcnorm, 'FFMC':ffmcnorm,'ISI':isinorm,'BUI':buinorm, 'FWI':fwinorm}
DF = pandas.DataFrame(raw_data, columns = ['FIRE_SIZE', 'DC', 'DMC', 'FFMC', 'ISI', 'BUI', 'FWI'])
DF.to_csv('fwi2015firesnormalized.csv')	

