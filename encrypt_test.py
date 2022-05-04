from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep
from datetime import datetime
import sys
import os
import json
import paho.mqtt.client as mqtt
import asyncio
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
import pgpy
username="ollie"
msgThread="test/wedtest"
my_private_key_file="my-private-key/myprikey.asc"
friendKeyFiles = []
friendPubKeys = []

#read in each file in the folder friend-public-key and store them in a list
for files in os.listdir("friend-public-key"):
    if files.endswith(".asc"):
        friendKeyFiles.append(files)

#print(len(friendKeyFiles))
#take each file from the list, make a temp key, and append it to a list
#might be able to combine these two
for i in range(len(friendKeyFiles)):
    print(i)
    temp, _ =pgpy.PGPKey.from_file("friend-public-key/"+friendKeyFiles[i])
    friendPubKeys.append(temp)
#make a test pgp message
msg=pgpy.PGPMessage.new("test msg")

#"encrypting messages to multiple recipients" section on pgpy docs
cipher = pgpy.constants.SymmetricKeyAlgorithm.AES256
sessionkey = cipher.gen_key()

#load in my own private key
priKey, _ = pgpy.PGPKey.from_file(my_private_key_file)

#msg must be encrypted by one key first, then the others are appended to it
for i in range(len(friendPubKeys)):
    if(i==0):
        enc_msg = friendPubKeys[i].encrypt(msg, cipher=cipher, sessionkey=sessionkey)
    else:
        enc_msg = friendPubKeys[i].encrypt(enc_msg, cipher=cipher, sessionkey=sessionkey)
#just printing it to files for testing
for i in range(len(friendPubKeys)):
    x=i+1
    with open("test"+str(x)+" encrypted msg", "w") as ff:
        ff.write(str(enc_msg))
#good practice to delete this session key after use
del sessionkey

print(enc_msg)
