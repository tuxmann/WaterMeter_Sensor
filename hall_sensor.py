# Hall effect sensor is connected to 5V & GND.
# OUT goes from GND to +2V. This should be sufficient to
# go from a logic HIGH to LOW. 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14, GPIO.IN)

#def my_callback(channel):
#  print "rotation detected"

time.sleep(2)

while True:
        if GPIO.input(14):
                print ("pin is HIGH")
        else:
                print ("pin is LOW")
        time.sleep(.5)                                              
