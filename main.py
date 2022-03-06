import paho.mqtt.client as mqtt

#Callback for connect
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker, code: "+str(rc))

#Callback for message receive
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("20.113.148.221", 1183, 60)

