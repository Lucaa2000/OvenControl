from m5stack import *
from m5ui import *
from uiflow import *
import machine
from easyIO import *
import time

setScreenColor(0x111111)


Temperate = None

#creating labels on the screen giving postion X, Y, name, font, temperature, rotation
label0 = M5TextBox(12, 27, "Temp", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=1)
Temperat = M5TextBox(9, 84, "------------", lcd.FONT_Default, 0xFFFFFF, rotate=0)
Heating = M5TextBox(13, 124, "Heating", lcd.FONT_Default, 0xFFFFFF, rotate=0)

from numbers import Number




while True:
  adc0 = machine.ADC(36) #creating A/D Converter and fixing it to pin 36
  adc0.width(machine.ADC.WIDTH_12BIT) #fixing range of A/D Converter in Bits
  adc0.atten(machine.ADC.ATTN_11DB) #setting A/D Converters atttenuation
  Temperate = (adc0.read()) / 37.6125 #calculating the Temperature in Celsius witht he Output value of the A/D Converter
  if Temperate != 0:
    Temperate = (Temperate if isinstance(Temperate, Number) else 0) + 1.5 #correcting minimal offset (continous component) in measured temeprature
  Temperat.setText(str(Temperate))
  if Temperate < 40:
    digitalWrite(26, 1) #set PIN 26 on HIGH (3.3 V)
    Heating.setColor(0xff0000)
  else:
    digitalWrite(26, 0) #set PIN 26 on LOW (0 V)
    Heating.setColor(0xffffff)
  wait(1)
  wait_ms(2)
