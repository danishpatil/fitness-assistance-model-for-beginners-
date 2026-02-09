import machine
import neopixel
import time
import urandom

# --- Setup ---
NUM_LEDS = 16
DATA_PIN = 4
np = neopixel.NeoPixel(machine.Pin(DATA_PIN), NUM_LEDS)

# Define our "Monotone" Pink and Purple palette
# Format: (Red, Green, Blue)
palette = [
    (255, 20, 147),  # Hot Pink
    (148, 0, 211),   # Dark Violet
    (75, 0, 130),    # Indigo
    (255, 105, 180), # Light Pink
    (128, 0, 128)    # Classic Purple
]

def clear():
    np.fill((0, 0, 0))
    np.write()

print("Starting Pink & Purple Monotone Show...")

try:
    while True:
        # 1. Pick a random color index from our palette
        # urandom.getrandbits(3) % 5 gives a number 0-4
        color_index = urandom.getrandbits(8) % len(palette)
        chosen_color = palette[color_index]
        
        # 2. Apply this color to all LEDs (Monotone effect)
        np.fill(chosen_color)
        np.write()
        
        # 3. Generate a random delay (between 0.2 and 1.2 seconds)
        # We use bits to create a random decimal
        random_decimal = urandom.getrandbits(10) / 1024
        delay = (random_decimal * 1.0) + 0.2
        
        print(f"Color: {chosen_color} | Delay: {delay:.2f}s")
        time.sleep(delay)

except KeyboardInterrupt:
    clear()
    print("Show stopped.")
    