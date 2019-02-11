import pandas as pd
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt

nc=Dataset('/home/rupak7/SABER_Temp_O3_May2002_v2.0.nc','r')

#print nc

lat=np.array(nc.variables['time'])
print lat.shape

lat2=np.array(nc.variables['tpaltitude'])
print lat2.shape


nc.close()
