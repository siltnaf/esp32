
from mqtt import MQTTClient
import ubinascii
from time import sleep
import machine


last_message = 0
message_interval = 10
counter = 0


# Complete project details at https://RandomNerdTutorials.com

def sub_cb(topic, msg):
  print((topic, msg))

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  
  
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  sleep(10)
  machine.reset()



try:
 
    client=MQTTClient(client_id, mqtt_server,1883)
    client.connect()
except OSError as e:
    restart_and_reconnect()

# eceived messages from subscriptions will be delivered to this callback
def sub_cb(topic_sub, msg):
    print((topic_sub, msg))
    

def main():

    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    while True:
        
        if client.check_msg()=='None':
            client.wait_msg()
        else:
            client.publish(topic_pub,'10')
            print(topic_pub)
            sleep(1)
        
    client.disconnect()

if __name__ == "__main__":
    main()