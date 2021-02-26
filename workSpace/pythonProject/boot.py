# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
try:
  import usocket as socket
except:
  import socket
import os
import gc
import network
from machine import Pin



led=Pin(22,Pin.OUT)

ap=network.WLAN(network.AP_IF)
ap.config(essid="QTurn", authmode=network.AUTH_OPEN)
ap.active(True)
ap.ifconfig()

#webserver=network.WLAN(network.STA_IF)
#webserver.active(True)
#webserver.connect('ken_2.4G','1233211234')

def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  with open ('webctrl.htm','r') as f:
      html=f.read()
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request=str(request)
    led_on=request.find('/?led=on')
    if led_on==6:
        led.value(1)
    print('Content = %s' % str(request))
    response = web_page()
    conn.send(response)
    conn.close()
