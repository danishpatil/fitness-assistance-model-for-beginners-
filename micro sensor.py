import time
from machine import Pin
led=Pin (2,Pin.OUT)
sensor=Pin (4,Pin.IN)
time.sleep(5)
led.on()
start=time.tricks_us()
while(1):
    sensorVal=sensor.value()
    if(sensorVal==0):
        end=time.ticks_us()
        print((end-start)/1000000)
        