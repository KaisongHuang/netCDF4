#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from netCDF4 import Dataset
import netCDF4 as nc
import numpy as np
from datetime import datetime


# In[ ]:


file_path = '../test/2100_r9i2p1r3.nc'


# In[ ]:


# Merge rlon, rlat, time
# Open files
all_file = Dataset(file_path, 'a')
part_file = Dataset('../test/huss_r9i2p1r3_final.nc', 'r') 

var_name = 'lon'
print('Appending variable {}'.format(var_name))
part_data = part_file[var_name][:]
all_file['rlon'][:] = part_data

var_name = 'lat'
print('Appending variable {}'.format(var_name))
part_data = part_file[var_name][:]
all_file['rlat'][:] = part_data

# Close files
all_file.close()
part_file.close()


# In[ ]:


# Merge time
# Open files
all_file = Dataset(file_path, 'a')
part_file = Dataset('../test/huss_r9i2p1r3_final.nc', 'r') 

var_name = 'time'
print('Appending variable {}'.format(var_name))
year = 2100
start = (year - 1951) * 2920
end = start + 2919
part_data = part_file[var_name]
all_data = all_file['time']
index = 0
for i in range(start, end + 1):
    all_data[index] = part_data[i]
    index += 1

# Close files
all_file.close()
part_file.close()


# In[ ]:


# Merge lon, lat
# Open files
all_file = Dataset(file_path, 'a')

rlon_data = all_file['rlon']
rlat_data = all_file['rlat']
lon_data = all_file['lon']
lat_data = all_file['lat']
print('Generating lon, lat')
for ilat in range(len(lon_data)):
    lon_data[ilat] = rlon_data[:]

for ilat in range(len(lat_data)):
    lat_data[ilat] = rlat_data[ilat]

# Close files
all_file.close()


# In[ ]:


# all_file = Dataset(file_path, 'a')

# # Set date
# dt = datetime(1952, 12, 31, 21, 0)

# # Get variable
# variable = all_file['time']
# data = variable[:]

# num = nc.date2num(dt, variable.units, variable.calendar)
# print('num: {}'.format(num))

# index = int(num/3)
# print('index: {}'.format(index))

# all_file.close()


# In[ ]:


# Merge huss
# Open files
print('Opening files...')
all_file = Dataset(file_path, 'a')
part_file = Dataset('../test/huss_r9i2p1r3_final.nc', 'r') 

var_name = 'huss'
print('Appending variable {}...'.format(var_name))
index = 0
for i in range(start, end + 1):
    all_file['hus'][index] = part_file[var_name][i]
    index += 1

# Close files
print('Closing files...')
all_file.close()
part_file.close()


# In[ ]:


# Merge pr
# Open files
print('Opening files...')
all_file = Dataset(file_path, 'a')
part_file = Dataset('../test/pr_r9i2p1r3_final.nc', 'r') 

var_name = 'pr'
print('Appending variable {}...'.format(var_name))
part_data = part_file[var_name]
all_data = all_file['pr']
index = 0
for i in range(start, end + 1):
    all_data[index] = part_data[i]
    index += 1

# Close files
print('Closing files...')
all_file.close()
part_file.close()


# In[ ]:


# Merge ps
# Open files
print('Opening files...')
all_file = Dataset(file_path, 'a')
part_file = Dataset('../test/ps_r9i2p1r3_final.nc', 'r') 

var_name = 'ps'
print('Appending variable {}...'.format(var_name))
part_data = part_file[var_name]
all_data = all_file['ps']
index = 0
for i in range(start, end + 1):
    all_data[index] = part_data[i]
    index += 1

# Close files
print('Closing files...')
all_file.close()
part_file.close()


# In[ ]:


# Merge rlds
# Open files
print('Opening files...')
all_file = Dataset(file_path, 'a')
part_file = Dataset('../test/rlds_r9i2p1r3_final.nc', 'r') 

var_name = 'rlds'
print('Appending variable {}...'.format(var_name))
part_data = part_file[var_name]
all_data = all_file['rlds']
index = 0
for i in range(start, end + 1):
    all_data[index] = part_data[i]
    index += 1

# Close files
print('Closing files...')
all_file.close()
part_file.close()


# In[ ]:


# Merge rsds
# Open files
print('Opening files...')
all_file = Dataset(file_path, 'a')
part_file = Dataset('../test/rsds_r9i2p1r3_final.nc', 'r') 

var_name = 'rsds'
print('Appending variable {}...'.format(var_name))
part_data = part_file[var_name]
all_data = all_file['rsds']
index = 0
for i in range(start, end + 1):
    all_data[index] = part_data[i]
    index += 1

# Close files
print('Closing files...')
all_file.close()
part_file.close()


# In[ ]:


# Merge wind_speed
# Open files
print('Opening files...')
all_file = Dataset(file_path, 'a')
part_file = Dataset('../test/sfcWind_r9i2p1r3_final.nc', 'r') 

var_name = 'sfcWind'
print('Appending variable {}...'.format(var_name))
part_data = part_file[var_name]
all_data = all_file['wind_speed']
index = 0
for i in range(start, end + 1):
    all_data[index] = part_data[i]
    index += 1

# Close files
print('Closing files...')
all_file.close()
part_file.close()


# In[ ]:


# Merge tas
# Open files
print('Opening files...')
all_file = Dataset(file_path, 'a')
part_file = Dataset('../test/tas_r9i2p1r3_final.nc', 'r') 

var_name = 'tas'
print('Appending variable {}...'.format(var_name))
part_data = part_file[var_name]
all_data = all_file['ta']
index = 0
for i in range(start, end + 1):
    all_data[index] = part_data[i]
    index += 1

# Close files
print('Closing files...')
all_file.close()
part_file.close()

print('Done!')

