from machine import Pin
import time
d=2

led=Pin(2,Pin.OUT)
led.on()
time.sleep(0.6*d)

led2=Pin(5,Pin.OUT)
led2.on()
time.sleep(0.5*d)

led3=Pin(18,Pin.OUT)
led3.on()
time.sleep(0.4*d)

led4=Pin(19,Pin.OUT)
led4.on()
time.sleep(0.3*d)

led5=Pin(21,Pin.OUT)
led5.on()
time.sleep(0.2*d)

led6=Pin(12,Pin.OUT)
led6.on()
time.sleep(0.1*d)


