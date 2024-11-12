import pyautogui
import time

print("Move your mouse around. Press Ctrl+C to stop.\n")

try:
    while True:
        # Get current mouse position
        x, y = pyautogui.position()
        print(f"Mouse at X: {x}, Y: {y}", end="\r")
        time.sleep(0.05)  # Slight delay to avoid flooding the output
except KeyboardInterrupt:
    print("\nProgram terminated.")
