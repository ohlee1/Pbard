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


#load in a test private key, decrypt the message, and print it out
priKey, _ = pgpy.PGPKey.from_file("test2-private.txt")
enc_msg = pgpy.PGPMessage.from_file("test2 encrypted msg")
print(enc_msg)
msg = priKey.decrypt(enc_msg).message
print("decrypted msg is: "+msg)