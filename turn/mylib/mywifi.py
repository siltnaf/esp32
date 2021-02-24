
##hardware platform: FireBeetle-ESP32


#Result: Blink


#The information below shows blink is unavailble for the current version.


#IO0 IO4 IO10 IO12~19 IO21~23 IO25~27


#Except the connection between IO2 and onboard LED, other pins need to connect to external LEDs.





from time import sleep


from machine import Pin

from mylib import mywifi




ssid="ken_5G"
password="1233211234"

mywifi.connect(ssid,password)

led=Pin(22,Pin.OUT)        #create LED object from pin2,Set Pin2 to output



while True:


  led.value(not led.value())


  sleep(0.5)







