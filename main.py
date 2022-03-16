import paho.mqtt.client as mqtt
import asyncio

#Callback for connect
def on_connect(client, userdata, flags, rc):
    #TODO
    #Add if else ladder for different result 'rc' codes e.g code 5 for unauthrorised
    print("Connected to MQTT broker, code: "+str(rc))

#Callback for message receive
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#Callback for publish
def on_publish(client, userdata, mid):
    #TODO
    #Make the published callback better
    print("Published")

#Callback for subscribe
def on_subscribe(client, userdata, mid, granted_qos):
    #TODO
    #Make the subscribed callback better
    print("Subscribed")

#Creating client object, giving client id and clean session to false to facilitate pulling of messages from broker
#TODO
#Work on making it pull from broker
client = mqtt.Client(client_id="liam", clean_session=False, userdata=None, transport="tcp")

#Setting up callbacks for the client object
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish

#Setting client to tls when enabled on Mosquitto
"""
client.tls_set()
"""


client.username_pw_set(username="user", password="Jmnb6014")

#async def main():

def main():

    #Debugging hivemq cluster for connectivity
    """
    client.connect("cefe654d7ef341e290b04311de927a20.s2.eu.hivemq.cloud", 8883, 60)
    """

    #General debugging as well as connectivity for the moment
    client.connect("52.232.13.39", 1883, 60)
    string = input("Please enter stuff here for topic: ")
    stringMsg = input("Please enter message: ")
    client.subscribe(string, qos=2)
    client.publish(string, stringMsg, qos=2, retain=True)
    
    #Network loop forever
    #TODO
    #Find a way to make it loop for subscribe for a certain length maybe with a counter/while loop?
    client.loop_forever()

if __name__ == '__main__':
    main()
#asyncio.run(main())
