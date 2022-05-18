from time import sleep
import json
import paho.mqtt.client as mqtt
import asyncio
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
import pgpy

username="ollie"
msgThread="test/wedtest"
#Callback for connect
def on_connect(client, userdata, flags, rc):
    #TODO
    #Add if else ladder for different result 'rc' codes e.g code 5 for unauthrorised
    print("Connected to MQTT broker, code: "+str(rc))

#Callback for message receive
def on_message(client, userdata, msg):
    y=msg.payload.decode()
#    print("payload is:", y)
#    recJson = msg.payload
#    print("json before strip:", recJson)
#    sleep(2)
#    recJson.lstrip("b\'").rstrip("\'")
#   print("json after strip:", recJson)
#    msg_in = json.loads(recJson)
#    sleep(5)
    #print(msg.topic+" "+str(msg.payload))
#    tempStr = str(msg.payload).lstrip("b\'").rstrip("\'")
#    tempStr.lstrip().rstrip()
#    print("tempStr is \n"+tempStr)
    sleep(0)
#    with open ("currentMsg.txt", "w") as x1:
#        x1.write(y)
    toDecrypt=pgpy.PGPMessage.from_blob(y)
#    with open ("currentMsg.txt", "w") as x1:
#        x1.write(tempStr)
#        json.dump(tempStr, x1)
#    toDecrypt=pgpy.PGPMessage.from_file("currentMsg.txt")
#    recStr = priKey.decrypt(toDecrypt)
#    recStr = recStr.lstrip("b\'").rstrip("\'")
#    print(recStr)
#    splStr = recStr.split(":")
#    print(splStr)
#    if(splStr[0] != username):#
#        print(recStr)
#    else:
#        print("", end="")
#    print("received:")
    final = priKey.decrypt(toDecrypt)
    finStr = str(final.message)
    splStr = finStr.split(":")
    if(splStr[0] != username):#
        print(finStr)
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

PRIVATE_KEY_FILE="testkey-private.txt"
priKey, _ = pgpy.PGPKey.from_file("testkey-private.txt")

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
#        client.publish(msgThread, stringMsg, qos=2, retain=False)
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
#            print("before msg.new")
            stringMsg = pgpy.PGPMessage.new(username+":"+stringMsg)
#            print("after msg.new")
            encryptedMsg = str(priKey.pubkey.encrypt(stringMsg))
#            print(encryptedMsg)
#            with open ("oldMsg.txt", "w") as x2:
#                x2.write(encryptedMsg)
#            print("after msg encrypt")
#            jsonMsg = json.dumps(encryptedMsg)
#            print(jsonMsg)
#            print("after json.dumps")
            client.publish(msgThread, encryptedMsg, qos=2, retain=False)
#            print("after publish")
            sleep(0)
#            print("encrypted msg is:", encryptedMsg)
#            sleep(2)
        
        #print(stringMsg)
    except:
        print("\nExiting")
    finally:
        client.loop_stop()
if __name__ == '__main__':
    main()
