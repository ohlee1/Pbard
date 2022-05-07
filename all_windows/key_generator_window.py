# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key-generator-window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm 
import sys, pgpy
from confirmation_window import Ui_Dialog

class Ui_keyGenWindow(QMainWindow):
    def setupUi(self, keyGenWindow):
        keyGenWindow.setObjectName("keyGenWindow")
        keyGenWindow.resize(800, 600)
        self.isOpen=True
        self.generateNotDone=True
        self.centralwidget = QtWidgets.QWidget(keyGenWindow)
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
        self.newKeyName = QtWidgets.QLineEdit(self.widget)
        self.newKeyName.setObjectName("newKeyName")
        self.gridLayout_2.addWidget(self.newKeyName, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.newKeyEmail = QtWidgets.QLineEdit(self.widget)
        self.newKeyEmail.setObjectName("newKeyEmail")
        self.gridLayout_2.addWidget(self.newKeyEmail, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.newKeyComment = QtWidgets.QLineEdit(self.widget)
        self.newKeyComment.setObjectName("newKeyComment")
        self.gridLayout_2.addWidget(self.newKeyComment, 2, 1, 1, 1)
        self.newKeyButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.generateKeyButton())
        self.newKeyButton.setObjectName("newKeyButton")
        self.gridLayout_2.addWidget(self.newKeyButton, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        keyGenWindow.setCentralWidget(self.centralwidget)
        self.window=keyGenWindow

        self.retranslateUi(keyGenWindow)
        QtCore.QMetaObject.connectSlotsByName(keyGenWindow)

    def retranslateUi(self, keyGenWindow):
        _translate = QtCore.QCoreApplication.translate
        keyGenWindow.setWindowTitle(_translate("keyGenWindow", "MainWindow"))
        self.label.setText(_translate("keyGenWindow", "Name: "))
        self.label_2.setText(_translate("keyGenWindow", "Email: "))
        self.label_3.setText(_translate("keyGenWindow", "Comment: "))
        self.newKeyButton.setText(_translate("keyGenWindow", "Generate new key"))

    def closeEvent(self, event):
        print("key gen window closed")
        self.isOpen=False
        try:
            self.newConfW.close()
        except:
            pass


    def generateKeyButton(self):
        #check to make sure username has been inputted, other two options aren't necessary
        #also check that a key hasn't been generated yet
        if(len(self.newKeyName.text())>0 and self.generateNotDone):
            key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
            username = self.newKeyName.text()
            email = self.newKeyEmail.text()
            comment = self.newKeyComment.text()
            uid = pgpy.PGPUID.new(username, comment=comment, email=email)
            key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
            hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
            ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
            compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed])
            with open("my-keys/myprikey.asc", "w") as f:
                f.write(str(key))
            with open("my-keys/"+username+"-public.asc", "w") as ff:
                ff.write(str(key.pubkey))
            self.generateNotDone=False
            #open confirmation window
            self.newConfW = Ui_Dialog()
            #call setup function inside the object
            self.newConfW.setupUi(self.newConfW)
            #send the window object and text into confirmation window
            self.newConfW.receiver(self.window, "Key Generated Successfully")
            #show the object
            self.newConfW.show()
        #if either no text inputted or key has been generated, go here
        else:
            #check boolean to see if key has been generated
            #if it has, tell user and pass
            if(not self.generateNotDone):
                print("key has been generated")
                pass
            #if key hasn't been generated tell user to enter a username
            else:
                print("Please enter a username")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_keyGenWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
