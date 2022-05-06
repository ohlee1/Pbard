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
import sys
import random, string



class Ui_newChatWindow(QMainWindow):
    def setupUi(self, newChatWindow):
        newChatWindow.setObjectName("newChatWindow")
        newChatWindow.resize(651, 606)
        self.count=1
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
        self.newChatStartButton = QtWidgets.QPushButton(self.widget)
        self.newChatStartButton.setObjectName("newChatStartButton")
        self.gridLayout_2.addWidget(self.newChatStartButton, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.newChatImportButton = QtWidgets.QPushButton(self.widget)
        self.newChatImportButton.setObjectName("newChatImportButton")
        self.gridLayout_2.addWidget(self.newChatImportButton, 4, 0, 1, 1)
        self.newChatName = QtWidgets.QLineEdit(self.widget)
        self.newChatName.setObjectName("newChatName")
        #as name is inputed mirror it to below box
        self.newChatName.textChanged.connect(self.updateUniqueName)
        self.gridLayout_2.addWidget(self.newChatName, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        newChatWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(newChatWindow)
        QtCore.QMetaObject.connectSlotsByName(newChatWindow)

    def retranslateUi(self, newChatWindow):
        _translate = QtCore.QCoreApplication.translate
        newChatWindow.setWindowTitle(_translate("newChatWindow", "MainWindow"))
        self.newChatStartButton.setText(_translate("newChatWindow", "Start New Chat"))
        self.label_3.setText(_translate("newChatWindow", "Unique thread name"))
        self.label.setText(_translate("newChatWindow", "Enter name of chat"))
        self.newChatImportButton.setText(_translate("newChatWindow", "Import Friends Public Keys"))

    def closeEvent(self, event):
        print("New chat window closed")
        self.count=0

    #when text is entered into the name box, copy it into the unique name box and append the topic extension to make it unique
    def updateUniqueName(self):
        temp = self.newChatName.text()
        self.lineEdit_2.setText(temp+"-"+self.topicExtension)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_newChatWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
