import pandas as pd
import numpy as np
from netCDF4 import Dataset
nc=Dataset('/home/rupak7/SABER_Temp_O3_April2002_v2.0.nc','r')
print nc  #summary of the netCDF file

print(nc.variables.keys())  #get all varibale names
lat=nc.variables['tplatitude'][:]  #latitude variable
#print lat

orb=nc.variables['orbit'][:]
print orb
print(nc.dimensions.keys()) #types of dimensions
for d in nc.dimensions.items():  #values of the dimensions
  	print(d)


# #every attribute has its own dimension and shape
print lat.dimensions
print lat.shape

# #each dimension typically has a variable associated with it

