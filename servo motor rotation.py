from machine import Pin, PWM
import time

# Initialize the Servo on GPIO 18
servo = PWM(Pin(18), freq=50)

def set_angle(angle):
    # Math: (angle / 180) * (max_duty - min_duty) + min_duty
    # We use 20 for 0 deg and 125 for 180 deg as a safe starting range
    duty = int((angle / 180) * (125 - 20) + 20)
    servo.duty(duty)

try:
    while True:
        print("Moving to 0 degrees")
        set_angle(0)
        time.sleep(1) # Wait for it to arrive
        
        print("Moving to 90 degrees")
        set_angle(90)
        time.sleep(0.5) # The "slight delay" you requested
        
        print("Moving to 180 degrees")
        set_angle(180)
        time.sleep(1)
        
        print("Resetting...")
        # Optional: Smoothly return or jump back to 0
        
except KeyboardInterrupt:
    # Safely turn off PWM when you stop the code
    servo.deinit()
    print("Servo detached.")
    