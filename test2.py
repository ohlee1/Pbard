from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep
from datetime import datetime
import sys
import json
import paho.mqtt.client as mqtt
import asyncio
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
import pgpy
username="ollie"
msgThread="test/wedtest"

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

class  Ui_MainWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

    def setupUI(self, MainWindow):

        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.pressButt())
        self.pushButton.setGeometry(QtCore.QRect(520, 340, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 320, 281, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.pressButt)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(210, 50, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        #menubar = self.menuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        fmenu = self.menubar.addMenu("File")
        fmenu.addAction(finish)
        self.menuAdd_friend = QtWidgets.QMenu(self.menubar)
        self.menuAdd_friend.setObjectName("menuAdd_friend")
        self.menustart_group_chat = QtWidgets.QMenu(self.menubar)
        self.menustart_group_chat.setObjectName("menustart_group_chat")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuAdd_friend.menuAction())
        self.menubar.addAction(self.menustart_group_chat.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #menubar = self.menuBar()
        #fmenu = menubar.addMenu("File")
        #fmenu.addAction(finish)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.menuAdd_friend.setTitle(_translate("MainWindow", "Add friend"))
        self.menustart_group_chat.setTitle(_translate("MainWindow", "start group chat"))

        
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
        stringMsg = pgpy.PGPMessage.new(niceDate+username+": "+stringMsg)
        encryptedMsg = str(priKey.pubkey.encrypt(stringMsg))
        client.publish(msgThread, encryptedMsg, qos=2, retain=False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    #MainWindow = QtWidgets.QMainWindow() fuck this line never use it
    MainWindow.setupUI(MainWindow)
    MainWindow.show()

    client.connect("52.232.13.39", 1883, 30)
    try:
        client.subscribe(msgThread, qos=2)
        client.loop_start()
    except:
        print("\nError subscribing to thread")

    sys.exit(app.exec_())
