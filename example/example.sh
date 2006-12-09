#!/bin/sh

# Read from the file
../tappy.py --filter usgs mayport_florida_8720220_data.txt mayport_florida_8720220_data_def.txt

# Read from COOPS web site data for 872-0218 Mayport Bar Pilots Dock
../tappy.py 'http://tidesandcurrents.noaa.gov/data_menu.shtml?bdate=20000101&bdate_Month=0&edate=20000401&edate_Month=1&wl_sensor_hist=W2&relative=&datum=6&unit=1&shift=&stn=8720218+Mayport+%28Bar+Pilots+Dock%29%2C+FL&type=Historic+Tide+Data&format=View+Data' tidesandcurrents.def

# Read from compressed file.  Use default 'sparse.def' parsing definition file.
../tappy.py tridentpier_florida_8721604_data.txt.gz

# Output
../tappy.py -o mayport_florida_8720220_data.txt mayport_florida_8720220_data_def.txt

# Filter wavelet
../tappy.py --aggressive-fit mayport_florida_8720220_data.txt mayport_florida_8720220_data_def.txt
