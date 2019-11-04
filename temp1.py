import gpiozero, readtemp
from time import sleep

while True:
  temp=readtemp.readtemp()

  print ( "Temp: {}c".format(temp) )

  sleep(0.1)
