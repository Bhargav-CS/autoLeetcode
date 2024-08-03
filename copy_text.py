import pyautogui
import time
import pyperclip
import os

# Give some time to switch to the desired window\

time.sleep(5)

# Move the mouse to the field (replace with actual coordinates)
field_x, field_y = 1210, 350
pyautogui.moveTo(field_x, field_y, duration=1)

# Click on the field
pyautogui.click()

# Press Ctrl + A to select all text
pyautogui.hotkey('ctrl', 'a')

# Press Ctrl + X to cut the selected text
pyautogui.hotkey('ctrl', 'x')

# Wait a moment for the clipboard to update
time.sleep(0.5)

# Get the text from the clipboard
copied_text = pyperclip.paste()





    
    


