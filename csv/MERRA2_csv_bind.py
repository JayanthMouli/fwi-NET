#EXTRACT MERRA DATA TO USABLE FORMAT (FLOAT AND CSV)


import csv
import datetime
import numpy as np
import os
from netCDF4 import Dataset


def core():
	dirname = '/home/jayanthmouli/Desktop/fire/netcdfreader/MERRA2'


	with open("datefix2015.csv", "r") as csvinput:
		with open("merrafires2015.csv", "w") as csvoutput:
			reader = csv.reader(csvinput)
			writer = csv.writer(csvoutput)
			d_reader = csv.DictReader(csvinput)
			headers = d_reader.fieldnames
			t_h = 'temperature (C)'
			rh_h = 'relative humidity (%)'
			wdspd_h = 'wind speed (km/h)'
			snw_h = 'snow depth (m)'
			headers.append(t_h)
			headers.append(rh_h)
			headers.append(wdspd_h)
			headers.append(snw_h)
			writer.writerow(headers)
			for row in reader:
				lat = float(row[8])
				lon = float(row[9])
				time = str(row[10])
				ary = row
				for filename in os.listdir(dirname):
					if filename.endswith(time+".nc"):
						f = Dataset(dirname+'/'+filename)
						lats = f.variables['lat'][:] 
						lons = f.variables['lon'][:]
						lat_idx = geo_idx(lat, lats)
	  					lon_idx = geo_idx(lon, lons)
						temp = str(f.variables['MERRA2_t'][:,lat_idx, lon_idx])
						tempcctd = temp[1:-1]
						rh = str(f.variables['MERRA2_rh'][:,lat_idx, lon_idx])
						rhcctd = rh[1:-1]
						wdspd = str(f.variables['MERRA2_wdSpd'][:,lat_idx, lon_idx])
						wdspdcctd = wdspd[1:-1]
						snw = str(f.variables['MERRA2_snowDepth'][:,lat_idx, lon_idx])
						snwcctd = snw[1:-1]
						ary.append(tempcctd)
						ary.append(rhcctd)
						ary.append(wdspdcctd)
						ary.append(snwcctd)
						writer.writerow(ary)
						break

def geo_idx(dd, dd_array):
	geo_idx = (np.abs(dd_array - dd)).argmin()
	return geo_idx
				
if __name__=='__main__':
	core()

	
