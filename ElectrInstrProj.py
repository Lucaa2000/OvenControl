# !/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt

TOPIC = "home/tutorial/PubSubDemo"
BROKER_ADDRESS = "broker.hivemq.com"
PORT = 1883


def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8")) #msg equals sent message
    print("message received: ", msg) 
    print("message topic: ", message.topic)
    #temp = float(msg)
    #print("msg as float: ", temp)
    
    if temp < 40:
        print("Heating")
    else:
        print("NOT_HEATING")
        

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker: " + BROKER_ADDRESS) #tells that subscription was sucessful
    client.subscribe(TOPIC) #subscribes to topic

if __name__ == "__main__": #actual script that runs
    client = mqtt.Client()
    client.on_connect = on_connect #jumps to def connect
    client.on_message = on_message #jumps to def message

    client.connect(BROKER_ADDRESS, PORT)  #client connects to BROKER_ADDRESS

    client.loop_forever() #loops infinite
        

    