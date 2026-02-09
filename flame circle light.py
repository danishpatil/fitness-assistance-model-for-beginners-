import machine, neopixel
import math
import time

# --- Configuration ---
PIN_NUM = 18          
NUM_PIXELS = 16       
pin = machine.Pin(PIN_NUM, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, NUM_PIXELS)

def hsv_to_rgb(h, s, v):
    if s == 0: return int(v), int(v), int(v)
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = int(v * (1.0 - s))
    q = int(v * (1.0 - s * f))
    t = int(v * (1.0 - s * (1.0 - f)))
    v = int(v)
    i %= 6
    if i == 0: return v, t, p
    if i == 1: return q, v, p
    if i == 2: return p, v, t
    if i == 3: return p, q, v
    if i == 4: return t, p, v
    if i == 5: return v, p, q

def run_timed_rotation():
    offset = 0.0
    # Higher FPS makes the rotation look buttery smooth
    fps = 30 
    sleep_time = 1 / fps
    
    # This controls how many seconds it takes for 1 full rotation
    seconds_per_rotation = 1.2  
    
    # Calculate how much to move the wave each frame
    # (2*PI is one full circle)
    step_size = (2 * math.pi) / (fps * seconds_per_rotation)

    print(f"Rotating every {seconds_per_rotation} seconds...")

    while True:
        for i in range(NUM_PIXELS):
            # i * (2*pi / NUM_PIXELS) spreads the wave perfectly across the ring
            pixel_phase = i * (2 * math.pi / NUM_PIXELS)
            wave = (math.sin(offset + pixel_phase) + 1) / 2
            
            # Colors: 0.0 (Red) -> 0.16 (Yellow)
            hue = wave * 0.16 
            
            # Rhythmic tone: Increasing intensity
            val = 40 + (wave * 200)
            
            r, g, b = hsv_to_rgb(hue, 1.0, val)
            np[i] = (r, g, b)
            
        np.write()
        
        offset -= step_size  # Use minus to go clockwise, plus for counter-clockwise
        time.sleep(sleep_time)

try:
    run_timed_rotation()
except KeyboardInterrupt:
    for i in range(NUM_PIXELS): np[i] = (0,0,0)
    np.write()