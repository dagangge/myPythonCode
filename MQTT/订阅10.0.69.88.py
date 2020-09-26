# encoding: utf-8 
import paho.mqtt.client as mqtt
 
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#")
 
 
def on_message(client, userdata, msg):
    print(msg.topic+" " + ":" + str(msg.payload))

client_id = "4945244"
client = mqtt.Client(client_id=client_id) 
client.on_connect = on_connect
client.on_message = on_message
#client.username_pw_set("admin","password")
client.connect("10.0.69.88", 8887, 60)
client.loop_forever()