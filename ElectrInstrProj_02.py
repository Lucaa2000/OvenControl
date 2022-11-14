# !/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt #importing mqtt library

#defining variable for mqtt connections
TOPIC = "TopicX"
BROKER_ADDRESS = "192.168.43.172"
PORT = 1883


def on_message(client, userdata, message): #call back for when message is received
    msg = str(message.payload.decode("utf-8")) #msg equals sent message
    print("message received: ", msg) 
    print("message topic: ", message.topic)
    temp = float(msg) #conversion because from string to float, beause I am not sure if the "if" comparison in line 18 works with strings
    print("msg as float: ", temp)
    
    if msg < 40:
        payload = 1
        print("Heating")
        publish.single(TOPIC, payload, 1) #publish payload=1 to TOPIC
    else:
        payload = 0
        print("NOT_HEATING")
        publish.single(TOPIC, payload, 1) #publish payload=0 to TOPIC
    #change payload to 0 or 1
        

def on_connect(client, userdata, flags, rc): #callback for when mqtt connected
    print("Connected to MQTT Broker: " + BROKER_ADDRESS) #tells that subscription was sucessful
    client.subscribe(TOPIC) #subscribes to topic everytime the device connects again (in case connection is lost)

if __name__ == "__main__": #actual script that runs
    client = mqtt.Client()
    client.on_connect = on_connect #jumps to def connect
    client.on_message = on_message #jumps to def message

    client.connect(BROKER_ADDRESS, PORT)  #client connects to BROKER_ADDRESS

    client.loop_forever() #loops forever
        

    