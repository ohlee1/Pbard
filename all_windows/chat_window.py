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
import sys


class Ui_chatWindow(QMainWindow):
    def setupUi(self, chatWindow):
        chatWindow.setObjectName("chatWindow")
        chatWindow.resize(698, 527)
        self.count = 1
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

        self.retranslateUi(chatWindow)
        QtCore.QMetaObject.connectSlotsByName(chatWindow)

        

    def closeEvent(self, event):
        print("chat window closed")
        self.count=0

    def retranslateUi(self, chatWindow):
        _translate = QtCore.QCoreApplication.translate
        chatWindow.setWindowTitle(_translate("chatWindow", "MainWindow"))
        self.loggingOff.setToolTip(_translate("chatWindow", "Chat messages will not be logged"))
        self.loggingOff.setText(_translate("chatWindow", "Chat logging off"))
        self.loggingOn.setToolTip(_translate("chatWindow", "Chat messages will be logged and stored in plaintext in the chat folder"))
        self.loggingOn.setText(_translate("chatWindow", "Chat Logging on"))
        self.sendChat.setText(_translate("chatWindow", "Send"))

    def setKeyFolder(self, keyFolder):
        self.keyFolder=keyFolder
        self.textBrowser.append(self.keyFolder)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_chatWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
