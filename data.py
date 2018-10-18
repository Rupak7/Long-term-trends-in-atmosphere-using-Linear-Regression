import pandas as pd
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

nc=Dataset('/home/rupak7/SABER_Temp_O3_April2002_v2.0.nc','r')
#print nc  #summary of the netCDF file


# print(nc.variables.keys())  #get all variable names
# lat1=nc.variables['tpgpaltitude']     #prints the masked array
# print lat1
# lat=np.array(nc.variables['tpaltitude'])  #latitude variable
# print lat
nc.close()


# clean_lat = []


# for j in range(len(lat)):        
#     clean_lat.append(lat[j])
#     for i in range(len(lat[j])):
#        if lat[j][i] > 1e+20:
#             clean_lat[j][i] = 0


# lat2 = np.array([item[:-1] for item in clean_lat])
# lat3 = [np.sum(item)/len(item)for item in lat2]
# lat3 = np.around(lat3,decimals=3,out=None)
# print lat3

# altitude=pd.DataFrame(lat3)

# altitude.to_hdf('April2002.h5',key='altitude',mode='a')

alt=pd.read_hdf('April2002.h5','altitude')

lat=pd.read_hdf('April2002.h5','latitude')

lon=pd.read_hdf('April2002.h5','longitude')

time=pd.read_hdf('April2002.h5','time')

temp = [alt, lat, lon, time]

# print temp

# temp = (lon - lat)/(time - alt) * alt 
# print temp

# plt.plot(temp,alt)
# plt.show()

with open('altitudeApril.txt', 'r') as f1:
    data1 = f1.read()

with open('latitudeApril.txt','r') as f:
    data = f.read()
#
res = [float(i) for i in data.split()]
res1 = [float(i) for i in data1.split()]
# #print res
position_lat = [index for index,element in enumerate(res) if element>22 and element<28]
#print position_lat
#

with open('longitudeApril.txt','r') as f2:
    data2 =  f2.read()
#
res2 = [float(i) for i in data2.split()]
# #print res
#
position_lon = [index for index,element in enumerate(res2) if element>86 and element<96]
#print position_lon

position = []
for i in position_lat:
    for j in position_lon:
        if i==j:
            position.append(i)
print position








