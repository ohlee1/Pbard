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
    y=msg.payload.decode()
    chatWindowob.recMsg(y)
    '''
    toDecrypt=pgpy.PGPMessage.from_blob(y)
    final = priKey.decrypt(toDecrypt)
    finStr = str(final.message)
    splStr = finStr.split(":")
    MainWindow.textBrowser.append(finStr)
    #if(splStr[0] != username):
    #    MainWindow.textBrowser.append(finStr)
    #    print(finStr)
    #else:
    #    print("", end="")
'''





#Setting client to tls when enabled on Mosquitto
"""
client.tls_set()
"""










class chatWinConn():

    def setupConn(self, settings, window, currentDir, keyFolder):
        global msgThread, MQTT_username, MQTT_serverIP, MQTT_serverPort, client, chatWindowob
        self.MQTT_settings=settings
        self.currentDir=currentDir
        self.friendPubKeys = []
        chatWindowob=window

        self.msgThread= self.MQTT_settings[0]
        self.MQTT_username = self.MQTT_settings[1]
        self.MQTT_serverIP = self.MQTT_settings[2]
        self.MQTT_serverPort = int(self.MQTT_settings[3])
        

        client = mqtt.Client(client_id=self.MQTT_username, clean_session=False, userdata=None, transport="tcp")

        #Setting up callbacks for the client object
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.on_publish = on_publish

        try:
            client.username_pw_set(username=self.MQTT_settings[4], password=self.MQTT_settings[5])
        except:
            pass
        '''
        self.priKey, _ = pgpy.PGPKey.from_file(self.currentDir+"my-keys/myprikey.asc")
        self.displayName = self.priKey.userids[0].name

        
        #read in each file in the folder friend-public-key and store them in a list
        for files in os.listdir(keyFolder):
            if files.endswith(".asc"):
                temp, _ =pgpy.PGPKey.from_file(keyFolder+"/"+files)
                self.friendPubKeys.append(temp)
'''        
        
        #client.connect("52.232.13.39", 1883, 30)
        client.connect(self.MQTT_serverIP, self.MQTT_serverPort, 30)
        try:
            client.subscribe(self.msgThread, qos=2)
            client.loop_start()
        except:
            print("REEEEE error subbing to thread")
        

    def printDetails(self):
        print(self.MQTT_settings)
        print(chatWindowob)

    def closeConn(self):
        client.loop_stop()
        client.disconnect()

    def sendMsg(self, pgpMsg):
        client.publish(self.msgThread, pgpMsg, qos=2, retain=False)

        

'''        
    def closeEvent(self, event):
        
        client.loop_stop()
        client.disconnect()
        print("Program closed and disconnected from server")

    def pressButt(self):
        stringMsg = self.lineEdit.text()
        self.lineEdit.clear()
        currentTime = datetime.now()
        dt_string = currentTime.strftime("%d/%m %H:%M")
        niceDate = "["+dt_string+"] "
        print(niceDate)
        #self.textBrowser.append(stringMsg)
        cipher = pgpy.constants.SymmetricKeyAlgorithm.AES256
        sessionkey = cipher.gen_key()
        stringMsg = pgpy.PGPMessage.new(niceDate+username+": "+stringMsg)
        for i in range(len(friendPubKeys)):
            if(i==0):
                enc_msg = friendPubKeys[i].encrypt(stringMsg, cipher=cipher, sessionkey=sessionkey)
            else:
                enc_msg = friendPubKeys[i].encrypt(enc_msg, cipher=cipher, sessionkey=sessionkey)

        enc_msg = priKey.pubkey.encrypt(enc_msg, cipher=cipher, sessionkey=sessionkey)
        del sessionkey
        encryptedMsg = str(enc_msg)
        client.publish(msgThread, encryptedMsg, qos=2, retain=False)
        '''

if __name__ == "__main__":
    print("test")
    
'''
    client.connect("52.232.13.39", 1883, 30)
    try:
        client.subscribe(msgThread, qos=2)
        client.loop_start()
    except:
        print("\nError subscribing to thread")
'''