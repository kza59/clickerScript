import pyautogui
import time

print("Move your mouse to the desired position and press Ctrl+C to set the click location.")

try:
    while True:
        x, y = pyautogui.position()
        position_str = f"X: {x} Y: {y}"
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nTerminated.")
    pyautogui.moveTo(x, y, duration=0.5)  
    pyautogui.click()  
    print(f"Click at X: {x}, Y: {y}")
