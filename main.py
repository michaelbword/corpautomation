import pyautogui
import time
import PIL
import cv2

# Setting input delay so code isn't too fast
pyautogui.PAUSE = 0.25

# Global variables defined for easier coding
click = pyautogui.click
type = pyautogui.typewrite
press = pyautogui.press
scroll = pyautogui.scroll
move = pyautogui.moveTo


def default():  # Opens menu and default apps, locates them, and changes them to the correct defaults
    try:
        windows = pyautogui.locateOnScreen('windows.png', grayscale=False, confidence=0.9)
        click(windows)
        type('Default Apps')
        press('enter')
        time.sleep(3)
        mail = pyautogui.locateOnScreen('mail.png', grayscale=False, confidence=0.9)  # Locates the mail icon
        click(mail)
        time.sleep(1)
        outlook = pyautogui.locateOnScreen('outlook.png', grayscale=True, confidence=0.7)  # Locates Outlook icon
        click(outlook)
        time.sleep(1)
        scroll(-5000)
        edge1 = pyautogui.locateOnScreen('edge.png', grayscale=False, confidence=0.7)  # Locate Edge icon
        click(edge1)
        time.sleep(1)
        chrome = pyautogui.locateOnScreen('chrome.png', grayscale=True, confidence=0.85)  # Locate Chrome icon
        click(chrome)
        defaults = pyautogui.locateOnScreen('defaults.png', grayscale=False, confidence=0.8)  # Moves pages
        click(defaults)
        time.sleep(3)
        adobe = pyautogui.locateOnScreen('finaladobes.png', grayscale=True, confidence=0.8)  # Locates Adobe Icon
        click(adobe)
        press('enter')
        press('tab')
        press('enter')
        edge1 = pyautogui.locateOnScreen('edge.png', grayscale=False, confidence=0.7)  # Locates Edge Icon
        click(edge1)
        press('space')
        press('enter')
    except:
        print("There seems to be an error. Please try again")
