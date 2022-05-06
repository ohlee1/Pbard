# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home-window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from new_chat_window import Ui_newChatWindow

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.count=0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.newChatButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.openNewChatWindow(MainWindow))
        self.newChatButton.setObjectName("newChatButton")
        self.verticalLayout.addWidget(self.newChatButton)
        self.openChatButton = QtWidgets.QPushButton(self.widget)
        self.openChatButton.setObjectName("openChatButton")
        self.verticalLayout.addWidget(self.openChatButton)
        self.newKeyButton = QtWidgets.QPushButton(self.widget)
        self.newKeyButton.setObjectName("newKeyButton")
        self.verticalLayout.addWidget(self.newKeyButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newChatButton.setText(_translate("MainWindow", "New Chat"))
        self.openChatButton.setText(_translate("MainWindow", "Open Existing Chat"))
        self.newKeyButton.setText(_translate("MainWindow", "Generate New Key"))

    def closeEvent(self, event):
        print("Program home screen closed")
        try:
            self.newChatW.close()
        except:
            pass

    def openNewChatWindow(self,MainWindow):
        try:
            if self.newChatW and self.newChatW.count>0:
                print("new chat window alreay open")
            else:
                self.newChatW = Ui_newChatWindow()
                self.newChatW.setupUi(self.newChatW)
                self.newChatW.show()
        except:
            self.newChatW = Ui_newChatWindow()
            self.newChatW.setupUi(self.newChatW)
            self.newChatW.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_MainWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
