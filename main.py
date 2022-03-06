import paho.mqtt.client as mqtt
import paho
import asyncio

#Callback for connect
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker, code: "+str(rc))

#Callback for message receive
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#Callback for publish
def on_publish(client, userdata, mid):
    print("Published")

#Callback for subscribe
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish

client.tls_set()

client.username_pw_set(username="JustAnotherLiam", password="Liamiot2021")


client.connect("cefe654d7ef341e290b04311de927a20.s2.eu.hivemq.cloud", 8883, 60)

print("ur mum")

client.subscribe("bruh/bruh", qos=0)
client.publish("bruh/bruh", "bruhbruhbruh", 0)
    
client.loop_forever()
