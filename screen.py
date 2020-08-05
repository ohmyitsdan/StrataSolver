import pyautogui
import time
from pyautogui import *
import keyboard
import random
import win32api, win32con
from PIL import Image
import win32api, win32con

end = (1680,780)
x = 1160
y = 240
w = end[1]-y
h = end[0]-x

colourpicker = {
    'purple': (145, 57, 88)
}
boxcolours = {
    'purple': (170, 130, 140),
    '-': (215, 211, 196) # BG
}
# purpcolour = 140-180,50-130,80-140
# lines = (181, 174, 153)
THRESHOLD = 18

grids = {
'grid2': {
    'box': {
    '1': (1340, 465),
    '2': (1440, 360),
    '3': (1535, 465),
    '4': (1440, 555)},
    'but': {
    '1': (1235, 570),
    '2': (1330, 665),
    '3': (1550, 665),
    '4': (1645, 570)}
}}


def click(but, grid, colour):
    # Select Colour
    for x in range(1200,1600,10):
        if pyautogui.pixel(x, 930) == colourpicker[colour]:
            win32api.SetCursorPos((x, 930))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.02)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    # Click Button
    butx, buty = grids[grid]['but'][but]
    win32api.SetCursorPos((butx,buty))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def read_screen(grid):
    this = grids[grid]['box']
    resp = []
    for x in this:        
        for y in boxcolours:
            if pyautogui.pixelMatchesColor(this[x][0], this[x][1], 
                (boxcolours[y]),tolerance=45):
                resp.append(y)
    return resp

def get_size():
    if pyautogui.locate('2grid.jpg', test_image, confidence=0.9):
        return 2
    else:
        return None

# while keyboard.is_pressed('q') == False:
#     pass