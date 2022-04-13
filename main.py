from time import sleep
import paho.mqtt.client as mqtt
import asyncio

username="frank"
msgThread="test/wedtest"
#Callback for connect
def on_connect(client, userdata, flags, rc):
    #TODO
    #Add if else ladder for different result 'rc' codes e.g code 5 for unauthrorised
    print("Connected to MQTT broker, code: "+str(rc))

#Callback for message receive
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    recStr = str(msg.payload)
    recStr = recStr.lstrip("b\'").rstrip("\'")
#    print(recStr)
    splStr = recStr.split(":")
#    print(splStr)
    if(splStr[0] != username):
        print(recStr)
    else:
        print("", end="")

#Callback for publish
def on_publish(client, userdata, mid):
    #TODO
    #Make the published callback better
    print("", end='')

#Callback for subscribe
def on_subscribe(client, userdata, mid, granted_qos):
    #TODO
    #Make the subscribed callback better
    print("Subscribed")

#Creating client object, giving client id and clean session to false to facilitate pulling of messages from broker
#TODO
#Work on making it pull from broker
client = mqtt.Client(client_id=username, clean_session=False, userdata=None, transport="tcp")

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
    client.connect("52.232.13.39", 1883, 30)
    try:
        #Debugging hivemq cluster for connectivity
        """
    client.connect("cefe654d7ef341e290b04311de927a20.s2.eu.hivemq.cloud", 8883, 60)
    """

        #General debugging as well as connectivity for the moment
        
        #string = input("Please enter stuff here for topic: ")
        #stringMsg = input("Please enter message: ")
        stringMsg = "testmsg:1"
        client.subscribe(msgThread, qos=2)
        client.publish(msgThread, stringMsg, qos=2, retain=False)
        client.loop_start()
        #Network loop forever
        #TODO
        #Find a way to make it loop for subscribe for a certain length maybe with a counter/while loop?
        #client.loop_forever()
        while True:
            #client.loop_forever()
            #sleep(1000)
            #client.loop_stop()
            stringMsg = input("")
            stringMsg = username+":"+stringMsg
            client.publish(msgThread, stringMsg, qos=2, retain=False)
        
        #print(stringMsg)
    except:
        print("Exiting")
    finally:
        client.loop_stop()
if __name__ == '__main__':
    main()
