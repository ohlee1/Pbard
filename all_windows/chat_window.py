# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat-window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, pgpy, datetime, os, mqtt_pBard
import paho.mqtt.client as mqtt
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
'''
def on_connect(client, userdata, flags, rc):
    #TODO
    #Add if else ladder for different result 'rc' codes e.g code 5 for unauthrorised
    #add error checking for address, maybe check config
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
    
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish
'''
class Ui_chatWindow(QMainWindow):
    def setupUi(self, chatWindow):
        chatWindow.setObjectName("chatWindow")
        chatWindow.resize(698, 527)
        self.count = 1
        self.friendPubKeys = []
        self.MQTT_settings = []
        self.centralwidget = QtWidgets.QWidget(chatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loggingOff = QtWidgets.QRadioButton(self.widget)
        self.loggingOff.setMaximumSize(QtCore.QSize(140, 16777215))
        self.loggingOff.setCheckable(True)
        self.loggingOff.setChecked(True)
        self.loggingOff.setObjectName("loggingOff")
        self.horizontalLayout.addWidget(self.loggingOff, 0, QtCore.Qt.AlignLeft)
        self.loggingOn = QtWidgets.QRadioButton(self.widget)
        self.loggingOn.setEnabled(True)
        self.loggingOn.setMaximumSize(QtCore.QSize(426, 16777215))
        self.loggingOn.setObjectName("loggingOn")
        self.horizontalLayout.addWidget(self.loggingOn, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.chatInputBox = QtWidgets.QLineEdit(self.widget)
        self.chatInputBox.setObjectName("chatInputBox")
        self.gridLayout_6.addWidget(self.chatInputBox, 2, 0, 1, 1)
        self.sendChat = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendChat.sizePolicy().hasHeightForWidth())
        self.sendChat.setSizePolicy(sizePolicy)
        self.sendChat.setObjectName("sendChat")
        self.gridLayout_6.addWidget(self.sendChat, 2, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_6.addWidget(self.textBrowser, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        chatWindow.setCentralWidget(self.centralwidget)
        self.window=chatWindow

        self.retranslateUi(chatWindow)
        QtCore.QMetaObject.connectSlotsByName(chatWindow)

        

        

    def closeEvent(self, event):
        print("chat window closed")
        self.count=0
        self.MQTTConn.closeConn()
        self.MQTTConn.close()

    def retranslateUi(self, chatWindow):
        _translate = QtCore.QCoreApplication.translate
        chatWindow.setWindowTitle(_translate("chatWindow", "MainWindow"))
        self.loggingOff.setToolTip(_translate("chatWindow", "Chat messages will not be logged"))
        self.loggingOff.setText(_translate("chatWindow", "Chat logging off"))
        self.loggingOn.setToolTip(_translate("chatWindow", "Chat messages will be logged and stored in plaintext in the chat folder"))
        self.loggingOn.setText(_translate("chatWindow", "Chat Logging on"))
        self.sendChat.setText(_translate("chatWindow", "Send"))

    def setKeyFolderAndSetupKeys(self, keyFolder, currentDir):
        #pass in key folder and current directory from where window was opened
        self.keyFolder=keyFolder
        self.currentDir=currentDir
        #strange behaviour with lstrip
        #uses chat folder name for the msg thread topic
        self.MQTT_settings.append(keyFolder.lstrip(currentDir).lstrip("chats"))

        #read in config file details
        with open(self.keyFolder+"/connection_details.conf", "r") as f:
            self.confDetails = f.readlines()
        for dtl in self.confDetails:
            self.MQTT_settings.append(dtl.split(":",1)[1].rstrip("\n"))

        print(self.MQTT_settings)
        print(self.window)

        self.MQTTConn = mqtt_pBard.chatWinConn()
        self.MQTTConn.setupConn(self.MQTT_settings, self.window, self.currentDir, self.keyFolder)
        self.MQTTConn.printDetails()

        '''
        #extract relevant information from file
        #first line is username, split once by : then take the username and remove the \n from the end
        #repeat for other details
        self.MQTTusername = self.confDetails[0].split(":",1)[1].rstrip("\n")
        self.MQTT_serverIP = self.confDetails[1].split(":",1)[1].rstrip("\n")
        self.MQTT_serverPort = self.confDetails[2].split(":",1)[1].rstrip("\n")
        #mqtt user settings for connection
        self.client = mqtt.Client(client_id=self.MQTTusername, clean_session=False, userdata=None, transport="tcp")
        #maybe move this try except into the connection one
        try:
            #if server username and password provided, add them to the client object
            self.MQTT_serverUsername = self.confDetails[3].split(":",1)[1].rstrip("\n")
            self.MQTT_serverPassword = self.confDetails[4].split(":",1)[1].rstrip("\n")
            self.client.username_pw_set(username=self.MQTT_serverUsername, password=self.MQTT_serverPassword)
        except:
            pass
            #no username or password set
        '''
        #import private key
        self.priKey, _ = pgpy.PGPKey.from_file(self.currentDir+"my-keys/myprikey.asc")


        #get name from prikey file to use as displayname
        self.displayName = self.priKey.userids[0].name
        #import friend keys
        for files in os.listdir(keyFolder):
            if files.endswith(".asc"):
                temp, _ =pgpy.PGPKey.from_file(keyFolder+"/"+files)
                self.friendPubKeys.append(temp)
        #connect to server and attempt to subscribe/start a network loop
        '''
        self.client.connect(self.MQTT_serverIP, self.MQTT_serverPort, 30)
        try:
            self.client.subscribe(self.msgThread, qos=2)
            self.client.loop_start()
        except:
            print("REEEEE error subbing to thread")
        '''

    def recMsg(self, pgpMsg):
        toDecrypt=pgpy.PGPMessage.from_blob(pgpMsg)
        final = self.priKey.decrypt(toDecrypt)
        finStr = str(final.message)
        self.window.textBrowser.append(finStr)

    def sendMsg(self):
        stringMsg = self.chatInputBox.text()
        self.chatInputBox.clear()
        currentTime = datetime.now()
        dt_string = currentTime.strftime("%d/%m %H:%M")
        niceDate = "["+dt_string+"] "
        #print(niceDate)
        #self.textBrowser.append(stringMsg)
        cipher = pgpy.constants.SymmetricKeyAlgorithm.AES256
        sessionkey = cipher.gen_key()
        stringMsg = pgpy.PGPMessage.new(niceDate+self.displayName+": "+stringMsg)
        for i in range(len(self.friendPubKeys)):
            if(i==0):
                enc_msg = self.friendPubKeys[i].encrypt(stringMsg, cipher=cipher, sessionkey=sessionkey)
            else:
                enc_msg = self.friendPubKeys[i].encrypt(enc_msg, cipher=cipher, sessionkey=sessionkey)

        enc_msg = self.priKey.pubkey.encrypt(enc_msg, cipher=cipher, sessionkey=sessionkey)
        del sessionkey
        #encryptedMsg = str(enc_msg)
        self.MQTTConn.sendMsg(str(enc_msg))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_chatWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
