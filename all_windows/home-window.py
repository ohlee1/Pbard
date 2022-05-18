import subprocess
import sys

#attempt to import all the modules
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from new_chat_window import Ui_newChatWindow
    from open_chat_window import Ui_openChatWindow
    from key_generator_window import Ui_keyGenWindow
    import pgpy
    import paho.mqtt.client as mqtt
#if it fails (pgpy, pyqt5, or paho mqtt not installed) then install them and attempt to import again
except ModuleNotFoundError as e:
    #Subprocess to execute pip command, install modules from requirements text file
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        from PyQt5 import QtCore, QtGui, QtWidgets
        from PyQt5.QtWidgets import *
        from PyQt5.QtCore import *
        from PyQt5.QtGui import *
        from new_chat_window import Ui_newChatWindow
        from open_chat_window import Ui_openChatWindow
        from key_generator_window import Ui_keyGenWindow
        import pgpy
        import paho.mqtt.client as mqtt
#if import still fails alert user
    except ModuleNotFoundError as f:
        print(f)
        print("Modules unable to be installed, please install manually!\n")


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        #qt designer code begin
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.windowList = []
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
        #added button reaction
        self.newChatButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.openNewChatWindow(MainWindow))
        self.newChatButton.setObjectName("newChatButton")
        self.verticalLayout.addWidget(self.newChatButton)
        self.openChatButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.openExistingChatWindow(MainWindow))
        self.openChatButton.setObjectName("openChatButton")
        self.verticalLayout.addWidget(self.openChatButton)
        self.newKeyButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.openKeyGeneratorWindow(MainWindow))
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
    #end qt designer code

    #close event, attempts to close the newchatw object when the main window is closed
    def closeEvent(self, event):
        print("Program home screen closed")
        for obj in self.windowList:
            obj.close()

    #when new chat window button is pressed, execute this
    def openNewChatWindow(self,MainWindow):
        #attempt to check if the object has been instantiated
        #if it doesn't exist, go to except and make it
        try:
            #check if the object exists and if it's currently open
            #isOpen will be set to true when instatiated and false when closed
            if self.newChatW and self.newChatW.isOpen:
                #if window is open and exists and isOpen is true, don't open a new one
                print("new chat window alreay open")
            else:
                #if window is closed and exists but isOpen is false, open a new one
                self.newChatW = Ui_newChatWindow()
                self.newChatW.setupUi(self.newChatW)
                self.newChatW.show()
                self.windowList.append(self.newChatW)
        except:
            #create new object
            self.newChatW = Ui_newChatWindow()
            #call setup function inside the object
            self.newChatW.setupUi(self.newChatW)
            #show the object
            self.newChatW.show()
            self.windowList.append(self.newChatW)

    def openExistingChatWindow(self,MainWindow):
        #attempt to check if the object has been instantiated
        #if it doesn't exist, go to except and make it
        try:
            #check if the object exists and if it's currently open
            #isOpen will be set to true when instatiated and false when closed
            if self.existingChatW and self.existingChatW.isOpen:
                #if window is open and exists and isOpen is true, don't open a new one
                print("existing chat window alreay open")
            else:
                #if window is closed and exists but isOpen is false, open a new one
                self.existingChatW = Ui_openChatWindow()
                self.existingChatW.setupUi(self.existingChatW)
                self.existingChatW.show()
                self.windowList.append(self.existingChatW)
        except:
            #create new object
            self.existingChatW = Ui_openChatWindow()
            #call setup function inside the object
            self.existingChatW.setupUi(self.existingChatW)
            #show the object
            self.existingChatW.show()
            self.windowList.append(self.existingChatW)

    def openKeyGeneratorWindow(self,MainWindow):
        #attempt to check if the object has been instantiated
        #if it doesn't exist, go to except and make it
        try:
            #check if the object exists and if it's currently open
            #isOpen will be set to true when instatiated and false when closed
            if self.keyGenW and self.keyGenW.isOpen:
                #if window is open and exists and isOpen is true, don't open a new one
                print("existing chat window alreay open")
            else:
                #if window is closed and exists but isOpen is false, open a new one
                self.keyGenW = Ui_keyGenWindow()
                self.keyGenW.setupUi(self.keyGenW)
                self.keyGenW.show()
                self.windowList.append(self.keyGenW)
        except:
            #create new object
            self.keyGenW = Ui_keyGenWindow()
            #call setup function inside the object
            self.keyGenW.setupUi(self.keyGenW)
            #show the object
            self.keyGenW.show()
            self.windowList.append(self.keyGenW)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    MainWindow = Ui_MainWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
