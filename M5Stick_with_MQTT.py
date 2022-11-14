from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import machine
import time
from easyIO import *

setScreenColor(0x111111)


PiMessage = None
Temperate = None

#creating labels on the screen 
label0 = M5TextBox(12, 18, "Temp", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=1)
PiMSG = M5TextBox(15, 134, "PiMSG", lcd.FONT_Default, 0xFFFFFF, rotate=0)
Temperat = M5TextBox(9, 60, "------------", lcd.FONT_Default, 0xFFFFFF, rotate=0)
Heating = M5TextBox(13, 100, "Heating", lcd.FONT_Default, 0xFFFFFF, rotate=0)

from numbers import Number



def fun_topicX_(topic_data): #defining topic to listen in on
  global PiMessage, Temperate 
  PiMessage = topic_data #set variable PiMessage to incoming data of given topic
  pass


m5mqtt = M5mqtt('M5Stick', '192.168.43.172', 1883, 'M5Stick', '12345678', 300) #setting up m5qtt publisher giving client id, server, port, user, password, timer
#probably you can define m5qtt = M5mqtt (...) with only the server, client and port 
m5mqtt.subscribe(str('topicX'), fun_topicX_) #setting up m5qtt subscriber (giving function to process incoming data)
m5mqtt.start() #starting up mqtt with given subscriber and publisher
while True:
  adc0 = machine.ADC(36) #creating A/D Converter and fixing it to pin 36
  adc0.width(machine.ADC.WIDTH_12BIT) #fixing range of A/D Converter in Bits
  adc0.atten(machine.ADC.ATTN_11DB) #setting A/D Converters atttenuation
  Temperate = (adc0.read()) / 37.6125 #calculating the Temperature in Celsius witht he Output value of the A/D Converter
  Temperat.setText(str(Temperate)) #set label Temperat on screen to the value of string Temperate
  m5mqtt.publish(str(Temperate),str('Temp sent')) #publishing value of "Temperate" with the indication "Temp sent" through the mqtt publisher
  wait(1)
  if PiMessage == 1:
    digitalWrite(26, 1)
    PiMSG.setText(str(PiMessage)) #indication to see what the Raspberry sent
    Heating.setColor(0xff0000)
  else:
    digitalWrite(26, 0)
    PiMSG.setText(str(PiMessage))  #indication to see what the Raspberry sent
    Heating.setColor(0xffffff)
  wait_ms(2)
