#THREADING TESTING

import threading
import paho.mqtt.client as mqtt

#Global variable for confirmed connection


#Callback for connect
def on_connect(client, userdata, flags, rc):
    #TODO
    #Add if else ladder for different result 'rc' codes e.g code 5 for unauthrorised
    print("Connected to MQTT broker, code: "+str(rc))

#Callback for message receive
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#Callback for publish
def on_publish(client, userdata, mid):
    #TODO
    #Make the published callback better
    print("Published")

#Callback for subscribe
def on_subscribe(client, userdata, mid, granted_qos):
    #TODO
    #Make the subscribed callback better
    print("Subscribed")

#Creating client object, giving client id and clean session to false to facilitate pulling of messages from broker
#TODO
#Work on making it pull from broker
client = mqtt.Client(client_id="liam", clean_session=False, userdata=None, transport="tcp")

#Setting up callbacks for the client object
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish

#Setting client to tls when enabled on Mosquitto
"""
client.tls_set()
"""


client.username_pw_set(username="user", password="Jmnb6014")

#async def main():

def main():

    #Debugging hivemq cluster for connectivity
    """
    client.connect("cefe654d7ef341e290b04311de927a20.s2.eu.hivemq.cloud", 8883, 60)
    """
    integerFlag = 1

    #General debugging as well as connectivity for the moment
    connectThread = threading.Thread(target=client.connect, args=("52.232.13.39",1883,30,))
    #client.connect("52.232.13.39", 1883, 30)
    print("Thread starting\n")
    connectThread.start()
    print("Thread started\n")
    connectThread.join()
    print("Thread finished\n")

    try:

        while True:
            userChoice = input("Input 1 for sending a message\nInput 2 for checking for messages\nInput 3 for subscribing to a new topic\nInput 0 to exit program\nOption: ")
            while integerFlag:
                try:
                    userChoice = int(userChoice)
                    integerFlag = 0
                except ValueError:
                    print("Please enter a integer...")
                    userChoice = input("Bruh pls\n")
                
            print(f"DEBUGGING USERCHOICE INIT WHILE: {userChoice}")

            while userChoice > 3 or userChoice < 0:
                    userChoice = int(input("Please enter 1 for sending a message\n2 for checking messages\n3 for subscribing to a topic\n0 to exit the program\nOption: "))
                    print(f"DEBUGGING USERCHOICE COMPARE WHILE: {userChoice}")









            if userChoice == 1:
                #topic = input("Please enter a topic: ")
                topic = "/bruh/bruh"
                stringMsg = input("Please enter message: ")
                client.publish(topic, stringMsg, qos=2, retain=False)
            
            elif userChoice == 3:
                topic = input("Input a topic: ")
                client.subscribe(topic, qos=2)
            
            elif userChoice == 2:
                #Network loop forever
                #TODO
                #Find a way to make it loop for subscribe for a certain length maybe with a counter/while loop?
                #LIAM: Implemented a small temporary solution using keyboard interrupt to allow check of messages and backout option, elegent solution required here
                try:
                    while True:
                        print("Checking for messages... Press CTRL+C to back out!")
                        client.loop_forever()
                except KeyboardInterrupt:
                    pass

            elif userChoice == 0:
                print("Exiting program...")
                exit(0)

            else:
                print(f"Unknown selector identified\nuserChoice == {userChoice}")
                print(f"Unknown selector identified\nuserChoice == {userChoice}")
                print(f"Unknown selector identified\nuserChoice == {userChoice}")
            integerFlag = 1
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)

if __name__ == '__main__':
    main()
#asyncio.run(main())
