import pyautogui
import time

# Defining global variables for easier code
click = pyautogui.click
type = pyautogui.typewrite
press = pyautogui.press
scroll = pyautogui.scroll
move = pyautogui.moveTo
kydown = pyautogui.keyDown
kyup = pyautogui.keyUp


def mount():
    try:
        kydown('win')
        press('r')
        kyup('win')
        type('cmd')
        press('enter')
        type('NET USE J: /d')
        press('enter')
        type('NET USE H: /d')
        press('enter')
        type('NET USE J: "\\\\fileserver\department folders"')
        press('enter')
        type('NET USE H: \\\\fileserver\public')
        press('enter')
    except:
        print("An error has occurred")
        pass
