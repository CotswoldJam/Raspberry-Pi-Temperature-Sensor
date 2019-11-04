import gpiozero, readtemp
from time import sleep

# Minimum and maximum temperatures
# Try changing these!
cold=22
hot=32

# Which pins are the LEDs connected to?
blueled=gpiozero.PWMLED(23)
redled=gpiozero.PWMLED(24)

# Turn on the LEDs
blueled.on()
redled.on()

while True:
  # Find the temperature
  temp=readtemp.readtemp()

  # Calculate a value between 0 and 1 representing hotness
  hotness=(temp-cold)/(hot-cold)
  if hotness>1:
    hotness=1
  if hotness<0:
    hotness=0
  print ( "Temp: {}c - Hotness {}".format(temp,hotness) )

  # Set the brightness of the LEDs
  blueled.value=1-hotness
  redled.value=hotness

  sleep(0.1)

