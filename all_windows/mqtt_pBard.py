from time import sleep
from datetime import datetime
import sys
import os
import paho.mqtt.client as mqtt
#from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
#import pgpy



def on_connect(client, userdata, flags, rc):
    #TODO
    #Add if else ladder for different result 'rc' codes e.g code 5 for unauthrorised
    print("Connected to MQTT broker, code: "+str(rc))

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

#Callback for message receive
def on_message(client, userdata, msg):
    #remove bytes characters and then pass to chat window to decrypt and display
    y=msg.payload.decode()
    chatWindowob.recMsg(y)



class chatWinConn():

    def setupConn(self, settings, window, currentDir, keyFolder):
        #declare global variables so that mqtt functions outside this class can use them
        global client, chatWindowob
        #save settings that were passed in
        self.MQTT_settings=settings
        #save current working directory that was passed in
        self.currentDir=currentDir
        #make list to append keys to later
        self.friendPubKeys = []
        #save chat window object that was passed in
        chatWindowob=window

        #extract settings from settings list
        self.msgThread= self.MQTT_settings[0]
        self.MQTT_username = self.MQTT_settings[1]
        self.MQTT_serverIP = self.MQTT_settings[2]
        self.MQTT_serverPort = int(self.MQTT_settings[3])
        
        #set client connection settings and username from conf file
        client = mqtt.Client(client_id=self.MQTT_username, clean_session=False, userdata=None, transport="tcp")

        #Setting up callbacks for the client object
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.on_publish = on_publish

        #try to set a username and password (if they're required/provided)
        try:
            client.username_pw_set(username=self.MQTT_settings[4], password=self.MQTT_settings[5])
        except:
            pass       
        
        #connect to server with ip and port from config file
        client.connect(self.MQTT_serverIP, self.MQTT_serverPort, 30)
        #attempt to subscribe to the thread
        try:
            client.subscribe(self.msgThread, qos=2)
            client.loop_start()
        except:
            print("error subbing to thread")
        
    #just for testing purposes
    def printDetails(self):
        print(self.MQTT_settings)
        print(chatWindowob)

    #all this to stop loop and close connection when exiting chat window
    def closeConn(self):
        client.loop_stop()
        client.disconnect()

    #pgp msg passed in from chat window and published here
    def sendMsg(self, pgpMsg):
        client.publish(self.msgThread, pgpMsg, qos=2, retain=False)

        



if __name__ == "__main__":
    print("test")
    