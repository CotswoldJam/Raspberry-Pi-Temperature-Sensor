# readtemp
# by Andrew Oakley 2016-07 Public Domain www.aoakley.com
# A module to read temperature in Celcius from a DS18B20 thermometer
# connected via the 1-Wire interface on a Raspberry Pi
# You must enable dtoverlay=w1-gpio in /boot/config.txt
# or enable 1-Wire interface in Preferences - Raspberry Pi Configuration
# Default pin is GPIO4
# Connect ground & 3.3V, then connect data wire to GPIO4

import glob
from time import sleep

# Initialise the private global variable
_readtemp_device_file=""

# Find the themometer file
def readtemp_init():
  global _readtemp_device_file
  base_dir = '/sys/bus/w1/devices/'
  glob_folder=glob.glob(base_dir + '28*')
  if len(glob_folder)<1:
    raise Exception("Cannot find DS18B20 thermometer")
  else:
    device_folder = glob_folder[0]
    _readtemp_device_file = device_folder + '/w1_slave'

# Read all the data from the thermometer
def _readtemp_raw():
  global _readtemp_device_file
  f = open(_readtemp_device_file, 'r')
  lines = f.readlines()
  f.close()
  return lines

# Extract the Celcius value from the thermometer data
def readtemp():
  if _readtemp_device_file == "":
    readtemp_init()

  lines = _readtemp_raw()
  tries = 0
  while lines[0].strip()[-3:] != 'YES' and tries<10:
    sleep(0.2)
    lines = _readtemp_raw()
    tries = tries+1
  if tries<10:
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0
      return temp_c
  else:
    raise Exception("Cannot get reading from DS18B20 thermometer")

