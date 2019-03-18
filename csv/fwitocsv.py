#using input NETCDF file from GFWED, use pandas Series to export each variable (column) as seperate csv files for testing purposes

import netCDF4
import pandas as pd

f = netCDF4.Dataset('/home/jayanthmouli/Desktop/fire/netcdfreader/FWI.MERRA2.CORRECTED.Daily.Default.20150131.nc')


lats = f.variables['lat'][:]
lons = f.variables['lon'][:]
dc = f.variables['MERRA2.CORRECTED_DC'][:]
dmc = f.variables['MERRA2.CORRECTED_DMC'][:]
ffmc = f.variables['MERRA2.CORRECTED_FFMC'][:]
isi = f.variables['MERRA2.CORRECTED_ISI'][:]
bui = f.variables['MERRA2.CORRECTED_BUI'][:]
fwi = f.variables['MERRA2.CORRECTED_FWI'][:]
time = f.variables['time']
dtime = netCDF4.num2date(time[:],time.units)


dc_ts = pd.Series(dc, index=dtime)
dmc_ts = pd.Series(dmc, index=dtime)
ffmc_ts = pd.Series(ffmc, index=dtime)
isi_ts = pd.Series(isi, index=dtime)
bui_ts = pd.Series(bui, index=dtime)
fwi_ts = pd.Series(fwi, index=dtime)

dc_ts.to_csv('dc.csv',index=True, header=True)
dmc_ts.to_csv('dmc.csv',index=True, header=True)
isi_ts.to_csv('isi.csv',index=True, header=True)
bui_ts.to_csv('bui.csv',index=True, header=True)
fwi_ts.to_csv('fwi.csv',index=True, header=True)
