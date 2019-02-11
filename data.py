import pandas as pd
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt


#nc=Dataset('/home/rupak7/SABER_Temp_O3_May2002_v2.0.nc','r')
#lat=np.array(nc.variables['tplatitude'])

#nc.close()

# clean_lat = []
# for j in range(len(lat)):
#    clean_lat.append(lat[j])
#    for i in range(len(lat[j])):
#       if lat[j][i] > 1e+20:
#          clean_lat[j][i] = 0
#
#
# lat2 = np.array([item[:-1] for item in clean_lat])
# lat3 = [np.sum(item)/len(item)for item in lat2]
# lat3 = np.around(lat3,decimals=3,out=None)
# print clean_lat

# # np.savetxt('tempMay.txt',lat3,fmt="%s")

with open('latitudeMay.txt','r') as f:
   data = f.read()
#
with open('longitudeMay.txt','r') as f1:
   data1 = f1.read()

with open('timeMay.txt','r') as f2:
   data3 = f2.read()
# # # #
# # #with open('altitude.txt','r') as f2:
# # #    data2 = f2.read()


res=np.array([float(i) for i in data.split()])
res1=np.array([float(i) for i in data1.split()])
res2=np.array([float(i) for i in data3.split()])

#res2=[float(i) for i in data2.split()]

# # # #position_lat = [index for index,element in enumerate(res) if element>22 and element<28]

# # # #position_lon = [index for index,element in enumerate(res1) if element>86 and element<96]


# res_new=[]
# res_new1=[]
# i=0
# #
# for i in range(len(res1)):
#     res.append(res1[i])



'''
fig,ax=plt.subplots()
ax.set_axisbelow(True)
ax.xaxis.set_ticks(np.arange(-180,181,40))
ax.yaxis.set_ticks(np.arange(0,25,3))
plt.plot(res,res1,'ro')
ax.grid(linestyle='-',linewidth='2',color='green')
plt.grid(True)
plt.show()
'''

# plt.title("May")
# plt.xlim(150,280)
# plt.ylim(10,110)
# plt.xlabel("Temperature")
# plt.ylabel("Altitude")
# plt.scatter(res_new1,res_new, s=1)
# plt.show()

#print len(res)

position = []

for i in res:
    for j in res1:
        if i==j:
            position.append(i)

for i in range(len(position)):
    position[i]=int(position[i])
# #
# time_cut=[]
lat1=[]
for i in position:
    lat1.append(res2[i])

print lat1

#np.savetxt('timeMay1.txt',lat1,fmt="%s")

#np.savetxt('temperature2.txt',res_new,fmt="%s")
