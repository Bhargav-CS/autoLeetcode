import pyautogui
import time

print("Move the cursor to the desired position and note the coordinates. Press Ctrl + C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Current position: x={x}, y={y}", end='\r')
        time.sleep(0.1)  # Update every 0.1 seconds
except KeyboardInterrupt:
    print("\nStopped.")
    
    
