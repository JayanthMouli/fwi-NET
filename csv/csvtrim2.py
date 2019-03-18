
#read large file as pandas dataframe, save as csv


import pandas as pd
fields = ['FIRE_YEAR', 'DISCOVERY_DATE','DISCOVERY_DOY', 'DISCOVERY_TIME', 'CONT_DOY' , 'FIRE_SIZE', 'FIRE_SIZE_CLASS' ,'LATITUDE' ,'LONGITUDE']

df = pd.read_csv('revised.csv', skipinitialspace=True, usecols=fields)
# See the keys
df.to_csv('aptcolumns.csv')
