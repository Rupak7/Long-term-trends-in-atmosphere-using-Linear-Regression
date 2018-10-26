import pandas as pd
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt

nc=Dataset('/home/rupak7/SABER_Temp_O3_May2002_v2.0.nc','r')
lat=np.array(nc.variables['tpaltitude'])
nc.close()

clean_lat = []
for j in range(len(lat)):
   clean_lat.append(lat[j])
   for i in range(len(lat[j])):
      if lat[j][i] > 1e+20:
         clean_lat[j][i] = 0


lat2 = np.array([item[:-1] for item in clean_lat])
lat3 = [np.sum(item)/len(item)for item in lat2]
lat3 = np.around(lat3,decimals=3,out=None)
print clean_lat

np.savetxt('tempMay.txt',lat3,fmt="%s")

with open('altitudeMay.txt','r') as f:
   data = f.read()
#
with open('temperature.txt','r') as f1:
   data1 = f1.read()
# # # #
# # #with open('altitude.txt','r') as f2:
# # #    data2 = f2.read()


res=np.array([float(i) for i in data.split()])
res1=np.array([float(i) for i in data1.split()])

#res2=[float(i) for i in data2.split()]

# # # #position_lat = [index for index,element in enumerate(res) if element>22 and element<28]

# # # #position_lon = [index for index,element in enumerate(res1) if element>86 and element<96]


res_new=[]
res_new1=[]
i=0

for i in range(len(res)):
    if res[i] != 0 and res1[i] != 0:
        res_new.append(res[i])
        res_new1.append(res1[i])


'''
while i < range(len(res1)):
    if (i == len(res1)):
        break
    if res1[i]==0:
        i+=1
    elif res1[i]<=150 and res1[i]>= 280:
        i+=1
    elif res[i]<=30 and res[i]>=100:
        i+=1
    else:
        res_new.append(res[i])
        res_new1.append(res1[i])
        i+=1
'''
#
# print res_new
#
#plt.xlim(150,280)
#plt.ylim(20,110)
plt.scatter(res_new1,res_new, s=1)
plt.show()

# # #print len(res)
# # #
# # #
# position = []
# # #
# for i in res:
#     for j in res1:
#         if i==j:
#             position.append(i)
# # #
# for i in range(len(position)):
#     position[i]=int(position[i])
# #
# time_cut=[]
# for i in position:
#     time_cut.append(clean_lat[i])

#np.savetxt('temperature2.txt',res_new,fmt="%s")
