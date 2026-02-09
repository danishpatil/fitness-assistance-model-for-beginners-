import machine
import neopixel
import time
import random

# --- Configuration ---
NUM_LEDS = 16
PIN_NEO = 14
PIN_SERVO = 13
PIN_IR = 27
PIN_BUTTON = 12

# Initialize Hardware
np = neopixel.NeoPixel(machine.Pin(PIN_NEO), NUM_LEDS)
ir_sensor = machine.Pin(PIN_IR, machine.Pin.IN)
button = machine.Pin(PIN_BUTTON, machine.Pin.IN, machine.Pin.PULL_UP)
servo = machine.PWM(machine.Pin(PIN_SERVO), freq=50)

def set_servo_angle(angle):
    # Duty cycle for 0 to 180 degrees (approx 40 to 115 for ESP32)
    duty = int(((angle / 180) * 75) + 40)
    servo.duty(duty)

def light_pattern():
    # Pick a random RGB color
    r = random.getrandbits(8)
    g = random.getrandbits(8)
    b = random.getrandbits(8)
    
    for i in range(NUM_LEDS):
        if i % 2 == 0:
            np[i] = (r, g, b)
        else:
            np[i] = (0, 0, 0) # Off
    np.write()

# Ensure start position
set_servo_angle(0)

print("System Ready...")

while True:
    # 1. Check IR Sensor (Active Low usually)
    if ir_sensor.value() == 0:
        print("Object Detected!")
        
        # 2. Move Servo to hit the button
        set_servo_angle(90)
        
        # 3. Check if button is pressed during movement
        # (Short delay to allow mechanical movement)
        time.sleep(0.3) 
        
        if button.value() == 0:
            print("Button Pressed by Servo!")
            light_pattern()
            
        # 4. Return Servo
        time.sleep(0.2)
        set_servo_angle(0)
        
        # Cool-down to prevent double-triggering
        time.sleep(1)