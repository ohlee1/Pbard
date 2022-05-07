# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open-chat-window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, os, shutil
from chat_window import Ui_chatWindow

class Ui_openChatWindow(QMainWindow):
    def setupUi(self, openChatWindow):
        openChatWindow.setObjectName("openChatWindow")
        openChatWindow.resize(800, 600)
        self.isOpen=True
        self.keyFilesList=[]
        self.centralwidget = QtWidgets.QWidget(openChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.openChatComboBox = QtWidgets.QComboBox(self.widget)
        self.openChatComboBox.setObjectName("openChatComboBox")
        self.gridLayout_2.addWidget(self.openChatComboBox, 1, 0, 1, 1)
        self.openChatAddKeyButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.importKeysButton())
        self.openChatAddKeyButton.setObjectName("openChatAddKeyButton")
        self.gridLayout_2.addWidget(self.openChatAddKeyButton, 2, 0, 1, 1)
        self.openChatStartButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.openChatButton())
        self.openChatStartButton.setObjectName("openChatStartButton")
        self.gridLayout_2.addWidget(self.openChatStartButton, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        openChatWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(openChatWindow)
        QtCore.QMetaObject.connectSlotsByName(openChatWindow)

        #code to get list of chats and display in combo box
        self.currentDir = os.getcwd()
        path1 = self.currentDir+"/all_chats/"
        path2 = self.currentDir+"/all_windows/all_chats/"

        #directory will depend on whether program has been launched from the py file or the bat/bash file
        #check if directory exists, returns a boolean
        if(os.path.isdir(path1)):
            self.chatDir = path1
        elif(os.path.isdir(path2)):
            self.chatDir = path2
        else:
            print("Error, no folder found for chats")
            self.close()
        
        self.chatList = os.listdir(self.chatDir)
        
        print(self.chatList)

        self.openChatComboBox = QtWidgets.QComboBox(self.widget)
        self.openChatComboBox.setObjectName("openChatComboBox")
        self.openChatComboBox.addItems(self.chatList)
        self.gridLayout_2.addWidget(self.openChatComboBox, 1, 0, 1, 1)

    def retranslateUi(self, openChatWindow):
        _translate = QtCore.QCoreApplication.translate
        openChatWindow.setWindowTitle(_translate("openChatWindow", "MainWindow"))
        self.label.setText(_translate("openChatWindow", "Select Chat"))
        self.openChatAddKeyButton.setText(_translate("openChatWindow", "Add Another Friend Key"))
        self.openChatStartButton.setText(_translate("openChatWindow", "Open Chat"))
        self.label_2.setText(_translate("openChatWindow", "Warning! Key files with the same name will be overwritten!"))

    def closeEvent(self, event):
        print("open existing chat window closed")
        self.isOpen=False

    def openChatButton(self):
        selection = self.chatList.index(self.openChatComboBox.currentText())
        #print(self.chatList[selection])
        #print(type(self.chatList[selection]))
        keyFolder = self.chatDir+self.chatList[selection]
        print(keyFolder)
        #check if any keys in the list
        if self.keyFilesList:
            #if keys present, then move them into the directory
            #iterate through list and copy the files into the folder
            for key in self.keyFilesList:
                #print(key)
                shutil.copy(key, keyFolder)
        

        #create new object
        self.chatW = Ui_chatWindow()
        #call setup function inside the object
        self.chatW.setupUi(self.chatW)
        #pass keyfolder name
        self.chatW.setKeyFolder(keyFolder)
        #show the object
        self.chatW.show()
        #maybe add code to create a json file with details??
        self.close()
        

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
        print(self.keyFilesList)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_openChatWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
