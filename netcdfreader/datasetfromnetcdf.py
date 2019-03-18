#export netcdf file to dataset

import numpy as np
import os
from netCDF4 import Dataset



f = Dataset('/home/jayanthmouli/Desktop/fire/netcdfreader/MERRA2/Wx.MERRA2.Daily.Default.20171227.nc')
lats = f.variables['lat'][:] 
lons = f.variables['lon'][:]
lat_bnds, lon_bnds = [32.8,42.1], [-125.7, -117.1]
latli = np.argmin( np.abs( lats - lat_bnds[0] ) )
latui = np.argmin( np.abs( lats - lat_bnds[1] ) ) 
lonli = np.argmin( np.abs( lons - lon_bnds[0] ) )
lonui = np.argmin( np.abs( lons - lon_bnds[1] ) )  
lon_inds = np.where((lons > lon_bnds[0]) & (lons < lon_bnds[1]))
temp_sub = f.variables['MERRA2_t'][:,latli:latui,lonli:lonui]
rh_sub = f.variables['MERRA2_rh'][:,latli:latui,lonli:lonui]
wdspd_sub = f.variables['MERRA2_wdSpd'][:,latli:latui,lonli:lonui]
swdpth_sub = f.variables['MERRA2_snowDepth'][:,latli:latui,lonli:lonui]
dataset = Dataset('/home/jayanthmouli/Desktop/fire/netcdfreader/trimmedMERRA2/FWI_trim.Wx.MERRA2.Daily.Default.20171227.nc', 'w',  format='NETCDF4_CLASSIC')
lat_carryover = f.variables['lat'][latli:latui]
lon_carryover = f.variables['lon'][lonli:lonui]
lat_new = dataset.createDimension('lat', len(lat_carryover))
lon_new = dataset.createDimension('lon', len(lon_carryover)) 
lats_new = dataset.createVariable('lats', np.float64, ('lat',))
lons_new = dataset.createVariable('lons', np.float64, ('lon',))
temp = dataset.createVariable('temp',np.float32 , ( 'lat', 'lon',))
rh = dataset.createVariable('rh', np.float32, ( 'lat', 'lon',))
wdspd = dataset.createVariable('wdspd', np.float32, ( 'lat', 'lon',))
swdpth = dataset.createVariable('swdpth', np.float32, ( 'lat', 'lon',))
latindices = np.where(32.8, 42.1, 0.1)
lonindices = np.where(-125.7, -117.1, 0.1)
lats_new[:] = lat_carryover
lons_new[:] = lon_carryover
temp[:] = temp_sub
rh[:] = rh_sub
wdspd[:] = wdspd_sub
swdpth[:] = swdpth_sub
dataset.close()		
