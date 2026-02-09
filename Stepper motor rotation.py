from machine import Pin

import time

in1=Pin(2,Pin.OUT)
in2=Pin(4,Pin.OUT)
in3=Pin(18,Pin.OUT)
in4=Pin(19,Pin.OUT)

delay=3

while(1):
    in1.off()
    in2.off()
    in3.off()
    in4.on()
    time.sleep_ms(delay)

    in1.off()
    in2.off()
    in3.on()
    in4.off()
    time.sleep_ms(delay)

    in1.off()
    in2.on()
    in3.off()
    in4.off()
    time.sleep_ms(delay)

    in1.on()
    in2.off()
    in3.off()
    in4.off()
    time.sleep_ms(delay)