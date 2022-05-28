import pyfirmata
from time import sleep
#assigning the port for Arduino
comport='COM4'

board=pyfirmata.Arduino(comport)

#led description
led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')

def led(total):
#if total number of fingers are 0 then no led and fan will turn ON
    if total == 0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

#if total number of fingers are 1 then fan and yellow led will turn ON
    elif total == 1:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

#if total number of fingers are 2 then fan and red led will turn ON
    elif total == 2:
        led_1.write(1)
        led_2.write(0)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)

#if total number of fingers are 3 then all leds will turn ON and fan will turn OFF
    elif total == 3:
        led_1.write(0)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)

#if total number of fingers are 4 then blue and yellow and fan will turn ON
    elif total == 4:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(1)
        led_5.write(1)

#if total number of fingers are 5 thn all leds and fan will turn ON
    elif total == 5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)


