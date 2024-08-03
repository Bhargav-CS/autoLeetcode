import pyperclip
import pyautogui
import time
import subprocess

while True:
    # Run Gemini_api.py
    subprocess.run(["python", "Gemini_api.py"])

    # Wait for some time before pasting new content
    
    time.sleep(5)

    # Read content from a specific file
    with open("solution.py", "r") as f:
        file_content = f.read()

    # Copy the file content to the clipboard
    pyperclip.copy(file_content)

    # Paste the file content into the field
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(3)

    submit_x, submit_y = 1838, 547
    pyautogui.moveTo(submit_x, submit_y, duration=1)
    pyautogui.click()

    time.sleep(10)

    next_x, next_y = 264, 148
    pyautogui.moveTo(next_x, next_y, duration=1)
    pyautogui.click()

    time.sleep(3)