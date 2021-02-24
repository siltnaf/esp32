import network

def connect(ssid,passwd):
    station=network.WLAN(network.STA_IF)
    if station.isconnected()==True:
        print("Already connected")
        return
    station.active(True)
    station.connect(ssid,passwd)
    while station.isconnected()==False:
        pass
    print('connection successful')
    print(station.ifconfig())