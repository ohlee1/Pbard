# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new-chat-window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from chat_window import Ui_chatWindow
import random, string, sys, os, shutil, pgpy


class Ui_newChatWindow(QMainWindow):
    def setupUi(self, newChatWindow):
        newChatWindow.setObjectName("newChatWindow")
        newChatWindow.resize(651, 606)
        self.isOpen=True
        self.keyFilesList=[]
        #generate random string of 10 digits to stick on the end of a topic name to make it unique
        self.topicExtension = ''.join(random.choices(string.digits, k=12))
        self.centralwidget = QtWidgets.QWidget(newChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.newChatStartButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.startNewChatButton())
        self.newChatStartButton.setObjectName("newChatStartButton")
        self.gridLayout_2.addWidget(self.newChatStartButton, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.uniqueTopicName = QtWidgets.QLineEdit(self.widget)
        self.uniqueTopicName.setObjectName("uniqueTopicName")
        self.gridLayout_2.addWidget(self.uniqueTopicName, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.newChatImportButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.importKeysButton())
        self.newChatImportButton.setObjectName("newChatImportButton")
        self.gridLayout_2.addWidget(self.newChatImportButton, 4, 0, 1, 1)
        self.newChatName = QtWidgets.QLineEdit(self.widget)
        self.newChatName.setObjectName("newChatName")
        #as name is inputed mirror it to below box
        self.newChatName.textChanged.connect(self.updateUniqueName)
        self.gridLayout_2.addWidget(self.newChatName, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        newChatWindow.setCentralWidget(self.centralwidget)
        self.window=newChatWindow

        self.retranslateUi(newChatWindow)
        QtCore.QMetaObject.connectSlotsByName(newChatWindow)

        #get the current directory and store it
        self.currentDir = os.getcwd()
        path1 = self.currentDir+"/all_chats/"
        path2 = self.currentDir+"/all_windows/all_chats/"

        #directory will depend on whether program has been launched from the py file or the bat/bash file
        #check if directory exists, returns a boolean
        if(os.path.isdir(path1)):
            self.chatDir = path1
            self.currentDir = self.currentDir+"/"
        elif(os.path.isdir(path2)):
            self.chatDir = path2
            self.currentDir = self.currentDir+"/all_windows/"
        else:
            print("Error, no folder found for chats")
            #open confirmation window
            self.newConfW = Ui_Dialog()
            #call setup function inside the object
            self.newConfW.setupUi(self.newConfW)
            #send the window object and text into confirmation window
            self.newConfW.receiver(self.window, "Error, no folder found for chats")
            #show the object
            self.newConfW.show()
        #get my private key and store it
        self.priKey, _ = pgpy.PGPKey.from_file(self.currentDir+"my-keys/myprikey.asc")


    def retranslateUi(self, newChatWindow):
        _translate = QtCore.QCoreApplication.translate
        newChatWindow.setWindowTitle(_translate("newChatWindow", "MainWindow"))
        self.newChatStartButton.setText(_translate("newChatWindow", "Start New Chat"))
        self.label_3.setText(_translate("newChatWindow", "Unique thread name"))
        self.label.setText(_translate("newChatWindow", "Enter name of chat"))
        self.newChatImportButton.setText(_translate("newChatWindow", "Import Friends Public Keys"))
        self.label_2.setText(_translate("newChatWindow", "Warning! Key files with the same name will be overwritten!"))

    def closeEvent(self, event):
        print("New chat window closed")
        self.isOpen=False

    #when text is entered into the name box, copy it into the unique name box and append the topic extension to make it unique
    def updateUniqueName(self):
        temp = self.newChatName.text()
        self.uniqueTopicName.setText(temp+"-"+self.topicExtension)

    def importKeysButton(self):
        #specify which file types to import
        fileFilter = 'Key File (*.asc)'
        #open window in current directory and ask user to select the public key files to import
        #self.keyFiles will be a tuple where the first item is a list of strings of the locations of the files, and the second item is the fileFilter variable
        self.keyFiles = QFileDialog.getOpenFileNames(
            parent=self,
            caption="Select key file(s)",
            directory=self.currentDir,
            filter=fileFilter
        )
        #append list of files to key files list
        self.keyFilesList.extend(self.keyFiles[0])
        #convert to dict and back to remove duplicates
        self.keyFilesList = list(dict.fromkeys(self.keyFilesList))
        #print(self.keyFilesList)

    def startNewChatButton(self):
        #new directory will but in the all_chats directory and will have the generated name
        newKeyFolder = self.chatDir+self.uniqueTopicName.text()
        #make the new directory
        #if running from pBard.sh the current directory will be where pBard.sh is, but all_chats is inside all_windows
        os.mkdir(newKeyFolder)
        #iterate through list and copy the files into the new folder
        for key in self.keyFilesList:
            #print(key)
            shutil.copy(key, newKeyFolder)
        #generate random string of numbers to use to make unique username
        self.usernameExtension = ''.join(random.choices(string.digits, k=12))
        #grab username from private key file
        keyUsername = self.priKey.userids[0].name
        #append numbers to username
        self.MQTTUsername = keyUsername+"-"+self.usernameExtension
        #write out server details and MQTT username to conf file, user can change these if they wish to use their own server
        with open(newKeyFolder+"/connection_details.conf", "w") as f:
                f.write("MQTT_username:"+self.MQTTUsername)
                f.write("\nMQTT_serverIP:"+"52.232.13.39")
                f.write("\nMQTT_serverPort:"+"1833")
                f.write("\nMQTT_serverUsername:"+"user")
                f.write("\nMQTT_serverPassword:"+"Jmnb6014")
        
        #create new object
        self.chatW = Ui_chatWindow()
        #call setup function inside the object
        self.chatW.setupUi(self.chatW)
        #pass keyfolder name
        self.chatW.setKeyFolder(newKeyFolder)
        #show the object
        self.chatW.show()
        #maybe add code to create a json file with details??
        self.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_newChatWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
