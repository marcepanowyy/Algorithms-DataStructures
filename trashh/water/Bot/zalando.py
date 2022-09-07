
from pyautogui import *

while True:
    x, y = locateCenterOnScreen("dostepny.PNG")
    if x and y:
        print("object found")

    print("object not found ")


