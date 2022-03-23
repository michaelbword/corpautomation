import pyautogui
import time
import PIL

# Defining functions for easier code
click = pyautogui.click
type = pyautogui.typewrite
press = pyautogui.press
scroll = pyautogui.scroll
move = pyautogui.moveTo
hold = pyautogui.hold
hotkey = pyautogui.hotkey
keyup = pyautogui.keyUp
keydown = pyautogui.keyDown


def chromework():  # Bookmarks service portal and shows bookmarks bar then installs webex
    try:
        windows = pyautogui.locateOnScreen('windows.png', grayscale=False, confidence=0.9)
        click(windows)
        type('Google Chrome')
        press('enter')
        time.sleep(2)
        type('mapcoexpress.service-now.com/mapco')
        press('enter')
        time.sleep(2)
        keydown('ctrl')
        keydown('shift')
        keydown('b')
        keyup('ctrl')
        keyup('shift')
        keyup('b')
        keydown('ctrl')
        keydown('d')
        keyup('ctrl')
        keyup('d')
        press('enter')
        click(306, 75)
        time.sleep(2)
        type('webex.com/downloads')
        press('enter')
        time.sleep(2)
        downloadlocation = pyautogui.locateOnScreen('webex.png', confidence=0.9)
        click(downloadlocation)
        print(downloadlocation)
    except:
        print("There seems to be an error")
        pass
