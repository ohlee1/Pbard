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
import sys


class Ui_openChatWindow(QMainWindow):
    def setupUi(self, openChatWindow):
        openChatWindow.setObjectName("openChatWindow")
        openChatWindow.resize(800, 600)
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
        self.openChatAddKeyButton = QtWidgets.QPushButton(self.widget)
        self.openChatAddKeyButton.setObjectName("openChatAddKeyButton")
        self.gridLayout_2.addWidget(self.openChatAddKeyButton, 2, 0, 1, 1)
        self.openChatStartButton = QtWidgets.QPushButton(self.widget)
        self.openChatStartButton.setObjectName("openChatStartButton")
        self.gridLayout_2.addWidget(self.openChatStartButton, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        openChatWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(openChatWindow)
        QtCore.QMetaObject.connectSlotsByName(openChatWindow)

    def retranslateUi(self, openChatWindow):
        _translate = QtCore.QCoreApplication.translate
        openChatWindow.setWindowTitle(_translate("openChatWindow", "MainWindow"))
        self.label.setText(_translate("openChatWindow", "Select Chat"))
        self.openChatAddKeyButton.setText(_translate("openChatWindow", "Add Another Friend Key"))
        self.openChatStartButton.setText(_translate("openChatWindow", "Open Chat"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_MainWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
