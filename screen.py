import pyautogui
import time
import keyboard
import win32api, win32con
from pyautogui import *
from PIL import Image
from bot import *
from coloursgrids import *

end = (1680,780)
x = 1160
y = 240
w = end[1]-y
h = end[0]-x

gameRegion = (960,0,960,1080)

def click(but, grid, colour, buttons):
    win32api.SetCursorPos((x, 930))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    # Click Button
    butx, buty = grids[grid]['but'][but]
    win32api.SetCursorPos((butx,buty))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def getSize():
    image = pyautogui.screenshot('img\\test.jpg',region=gameRegion)
    rotated = Image.open('img\\test.jpg').rotate(-45).save('img\\rotated.jpg')
    if pyautogui.locate('img\\2grid.jpg', 'img\\rotated.jpg', confidence=0.9):
        return 2
    else:
        return None

def makeList(gridSize, colours):
    ct = 0
    grid = []
    row = []
    row1 = []
    if len(colours) == 1:
        for i in range(gridSize):
            row.append(colours[0])
        for j in range(gridSize):
            grid.append(row)
        return grid
    for i in range(gridSize):
        row.append(colours[i])
        row1.append(colours[i+gridSize])
    grid.append(row)
    grid.append(row1)
    return grid

def buttonColour(gridSize):
    inPlay = []
    colourList = []
    this = grids['grid'+str(gridSize)]['pick']
    for x in this:
        pix = pyautogui.pixel(x[0],x[1])
        inPlay.append(pix)
    for a in inPlay:
        for key,val in colourpicker.items():
            if compare(a,val):
                colourList.append(key.upper())
    return colourList

def coloursInPlay(gridSize):
    inPlay = []
    colourList = []
    this = grids['grid'+str(gridSize)]['box']
    for x in this:
        pix = pyautogui.pixel(x[0],x[1])
        inPlay.append(pix)
    for a in inPlay:
        for key,val in boxcolours.items():
            if compare(a,val):
                colourList.append(key)
    return colourList

def makeGrids():
    gridSize = getSize()
    colours = coloursInPlay(gridSize)
    grid = makeList(gridSize, '-')
    board = makeList(gridSize, colours)
    for x in colours:
        if x == '-':
            colours.remove(x)
    return grid, board, colours

def pixelTest(colA, colB):
    return colA - colB in range(-20,20)

def compare(a, b):
    if pixelTest(a[0], b[0]):
        if pixelTest(a[1], b[1]):
            if pixelTest(a[2], b[2]):
                return True
    return False

def play():
    gridSize = getSize()
    grid, board, colours = makeGrids()
    buttons = buttonColour(gridSize)

    seq = solve(grid, board, colours, [])
    
    # print(board)
    # print('Colours:', colours)
    # print('buttons:', buttons)
    # print('seq:', seq)
    # for x in seq:
    #     click(x[0], gridSize, x[1])


gridSize = getSize()
blank, board, colours = makeGrids()
buttons = buttonColour(gridSize)
thisgrid = grids['grid2']['grid']
print(blank)
print(inb)
print('blank == inb:', blank == inb)
print(board)
print(mat)
print(colours)
seq1 = solve(blank, board, colours, [])
seq2 = solve(inb, board, colours, [])
print(seq1)
print(seq2)
# play()

