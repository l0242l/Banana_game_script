# banana
"""
if these imports are red install them by typing
" pip install (the thing that is red)" 
into the terminal 

"""

from AppOpener import open, close
import time
import math
from pynput.mouse import Button, Controller
import tkinter as tk
import cv2
import numpy as np
import pyautogui

mouse = Controller()
app = "banana"

# opens banana game
time.sleep(2)

open(app)
time.sleep(5)
def MouseShit():
    pos = mouse.position
    print(pos,"\n")
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    goal_x = screen_width / 2
    goal_y = screen_height / 2
    x = goal_x - pos[0]
    y = goal_y - pos[1]
    print(x,y)
    mouse.move(x, y)
    time.sleep(10)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(.1)

def find_and_click_banana():
    # Load banana image
    banana_img = cv2.imread('banana.png')
    # Convert image to grayscale
    banana_gray = cv2.cvtColor(banana_img, cv2.COLOR_BGR2GRAY)

    # Capture screen
    screen = pyautogui.screenshot()
    screen = np.array(screen)
    # Convert screenshot to grayscale
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

    # Match banana template on the screen
    res = cv2.matchTemplate(screen_gray, banana_gray, cv2.TM_CCOEFF_NORMED)
    # Set a threshold to consider it a match
    threshold = 0.8
    loc = np.where(res >= threshold)

    # Click on the center of each matched region
    for pt in zip(*loc[::-1]):
        # Calculate center coordinates
        center_x = pt[0] + banana_img.shape[1] // 2
        center_y = pt[1] + banana_img.shape[0] // 2
        # Simulate mouse click
        pyautogui.click(x=center_x, y=center_y)
        print("Clicked on banana!")
        break

find_and_click_banana()
#MouseShit()
close(app)
