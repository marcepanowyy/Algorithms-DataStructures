from pyautogui import *

while True:
    sleep(10)
    press("f5")
    sleep(8)
    x1, y1 = locateCenterOnScreen("wybierz_rozmiar.PNG")
    moveTo(x1, y1, duration=1)
    leftClick()
    sleep(300)