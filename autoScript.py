import pyautogui
import time
import subprocess
import psutil
import os
import subprocess
import logging
import config
from config import PATH_NAME, PROCESS_NAME, BUTTON_X, BUTTON_Y

app_path = PATH_NAME

def move_cursor(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
subprocess.Popen([app_path])

def kill_process(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            proc.kill()
            print(f"Process '{process_name}' has been terminated.")
            return
    print(f"No process with name '{process_name}' found.")
time.sleep(8)

button_x, button_y = BUTTON_X, BUTTON_Y
move_cursor(button_x, button_y)
pyautogui.click(button_x, button_y)

time.sleep(60)

pyautogui.hotkey('alt', 'f4')

if __name__ == "__main__":
    process_name = PROCESS_NAME
    kill_process(process_name)
