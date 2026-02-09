from machine import Pin
import time

led=Pin(4,Pin.OUT)
led2=Pin(5,Pin.OUT)

times=15

counter=0

while(counter<times):
    led.on()
    led2.on()
    time.sleep(.3)
    led.off()
    led2.off()
    time.sleep(.3)
    counter=counter+1
    
 
 
 
