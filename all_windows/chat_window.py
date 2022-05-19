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

class Ui_chatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, chatWindow):
        chatWindow.setObjectName("chatWindow")
        chatWindow.resize(698, 527)
        self.count = 0
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
        self.chatInputBox.returnPressed.connect(self.sendMsg)
        self.gridLayout_6.addWidget(self.chatInputBox, 2, 0, 1, 1)
        self.sendChat = QtWidgets.QPushButton(self.widget, clicked=lambda: self.sendMsg())
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
        #self.count=0
        #stop network loop and close connection to mqtt server
        self.MQTTConn.closeConn()

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

        #print(self.MQTT_settings)
        #print(self.window)

        #instantiate mqtt connection object and pass details into the setup
        self.MQTTConn = mqtt_pBard.chatWinConn()
        self.MQTTConn.setupConn(self.MQTT_settings, self.window, self.currentDir, self.keyFolder)
        self.MQTTConn.printDetails()

        #import private key
        self.priKey, _ = pgpy.PGPKey.from_file(self.currentDir+"my-keys/myprikey.asc")


        #get name from prikey file to use as displayname
        self.displayName = self.priKey.userids[0].name
        #import friend keys
        for files in os.listdir(keyFolder):
            if files.endswith(".asc"):
                temp, _ =pgpy.PGPKey.from_file(keyFolder+"/"+files)
                self.friendPubKeys.append(temp)
        
    #when a msg is received it's passed in here to be decrypted and printed out
    def recMsg(self, pgpMsg):
        #convert str to pgp msg object
        toDecrypt=pgpy.PGPMessage.from_blob(pgpMsg)
        #decrypt it
        final = self.priKey.decrypt(toDecrypt)
        #pull out the msg
        finStr = str(final.message)
        #display the msg
        self.textBrowser.append(finStr)
        self.textBrowser.moveCursor(QTextCursor.End)

    #called when message is being sent (enter pressed or send button)
    def sendMsg(self):
        #grab string from chat input box and clear it
        stringMsg = self.chatInputBox.text()
        self.chatInputBox.clear()
        #get current date and time and pull out the nice bits
        currentTime = datetime.datetime.now()
        dt_string = currentTime.strftime("%d/%m %H:%M")
        niceDate = "["+dt_string+"] "
        #create a session key for encrypting with
        cipher = pgpy.constants.SymmetricKeyAlgorithm.AES256
        sessionkey = cipher.gen_key()
        #create the pgp msg with the date/time and displayname and the message
        stringMsg = pgpy.PGPMessage.new(niceDate+self.displayName+": "+stringMsg)
        #encrypt using your own public key first, then your friends public keys if you have them
        enc_msg = self.priKey.pubkey.encrypt(stringMsg, cipher=cipher, sessionkey=sessionkey)
        for i in range(len(self.friendPubKeys)):
            if(i==0):
                enc_msg = self.friendPubKeys[i].encrypt(enc_msg, cipher=cipher, sessionkey=sessionkey)
            else:
                enc_msg = self.friendPubKeys[i].encrypt(enc_msg, cipher=cipher, sessionkey=sessionkey)
        #delete the session key (good practice) 
        del sessionkey
        #send to the mqtt connection file to send out to the server
        self.MQTTConn.sendMsg(str(enc_msg))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_chatWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat-window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

