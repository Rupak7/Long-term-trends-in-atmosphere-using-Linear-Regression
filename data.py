import pandas as pd
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

nc=Dataset('/home/rupak7/SABER_Temp_O3_April2002_v2.0.nc','r')
print nc  #summary of the netCDF file

print(nc.variables.keys())  #get all varibale names
lat=nc.variables['tplatitude'][:]  #latitude variable
print lat

orb=nc.variables['orbit'][:]
print orb
print(nc.dimensions.keys()) #types of dimensions
for d in nc.dimensions.items():  #values of the dimensions
  	print(d)


#every attribute has its own dimension and shape
print lat.dimensions
print lat.shape

# #each dimension typically has a variable associated with it

fig = plt.figure(num=None, figsize=(12, 8) )
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='tan',lake_color='lightblue')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.),labels=[True,True,False,False],dashes=[2,2])
m.drawmeridians(np.arange(-180.,181.,60.),labels=[False,False,False,True],dashes=[2,2])
m.drawmapboundary(fill_color='lightblue')
plt.title("Mercator Projection")
plt.show()
