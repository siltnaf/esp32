import time
from machine import Pin
led=Pin(22,Pin.OUT)        #create LED object from pin2,Set Pin2 to output

while True:
  led.value(1)            #Set led turn on
  time.sleep(1)
  led.value(0)            #Set led turn off
  time.sleep(1)