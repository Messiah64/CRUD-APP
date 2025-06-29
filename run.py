import pyautogui
import time
import random

# Load words from your text file
with open('words.txt', 'r') as file:
    words = [line.strip() for line in file if line.strip()]

print("Typing + mouse activity started. Make sure your VSCode editor is focused.")

try:
    while True:
        # Simulate typing a random word
        word = random.choice(words)
        pyautogui.write(word + ' ', interval=0.05)

        # Obvious mouse movement in zig-zag
        x_offset = random.choice([100, -100])
        y_offset = random.choice([50, -50])
        pyautogui.moveRel(x_offset, y_offset, duration=0.3)

        time.sleep(1)  # Wait 1 second
except KeyboardInterrupt:
    print("Stopped.")