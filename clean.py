import pandas as pd
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt

nc=Dataset('/home/rupak7/SABER_Temp_O3_May2002_v2.0.nc','r')
lat=np.array(nc.variables['time'])
#print lat

#
clean_lat = []
for j in range(len(lat)):
   clean_lat.append(lat[j])
   for i in range(len(lat[j])):
      if lat[j][i] < 0:
         clean_lat[j][i] = 0
#
#
lat2 = np.array([item[:-1] for item in clean_lat])
#lat3 = np.array([np.sum(item)/len(item)for item in lat2])
lat4 = lat2/float(3600000)
print lat4.shape
lat3 = np.around(lat4,decimals=5,out=None)
np.savetxt('timeMay.txt',lat3,fmt="%s")
print lat3
nc.close()
