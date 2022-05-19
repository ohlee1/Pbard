# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmation-window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
#from key_generator_window import Ui_keyGenWindow

class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(303, 122)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.pushButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.OKPressed())
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QIcon("icons/checkMark.png"))
        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "text here"))
        self.pushButton.setText(_translate("Dialog", "OK"))

    def OKPressed(self):
        self.close()

    def closeEvent(self, event):
        print("Closed ok box window")
        try:
            self.currentWindow.close()
        except:
            print("no other window to close")
            pass


    def receiver(self, recWindow, displayText):
        self.label_2.setText(displayText)
        self.currentWindow=recWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = Ui_Dialog()
    Dialog.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())