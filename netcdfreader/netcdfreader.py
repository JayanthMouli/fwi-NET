#convenience print variables from nc file

from netCDF4 import Dataset
dset = Dataset('/home/jayanthmouli/Desktop/fire/netcdfreader/FWI.MERRA2.CORRECTED.Daily.Default.20150131.nc')
print dset.variables
