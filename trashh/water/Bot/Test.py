# from pyautogui import *


# class Clicker:
#     def __init__(self, target_png, speed):
#         self.target_png = target_png
#         self.speed = speed
#         FAILSAFE = True
#
#     def nav_to_image(self):
#         try:
#             position = locateCenterOnScreen(self.target_png, confidence=.8)
#             moveTo(position[0], position[1], duration=self.speed)
#             click()
#         except:
#             print('No image found...')
#             return 0
#
# sleep(2)
#
# clicker = Clicker('Images/circle.png', speed=.01)
#
# end = 0
#
# while True:
#     if clicker.nav_to_image() == 0:
#         end += 1
#
#     if end > 20:
#         break

from pyautogui import *

# C:\Users\Pawel\PycharmProjects\pythonProject3\Images\skrin.PNG
# skrin.PNG
# Images/skrin.PNG

# cords = locateCenterOnScreen('Images/CircleV2.PNG')
# sleep(1)
# click(cords)
# print(cords)
# moveTo(cords[0], cords[1], 0.1)
# doubleClick()

# while True:
#     if locateCenterOnScreen('Images\stickman.png') != None:
#         print('I can see it')
#         sleep(0.5)
#     else:
#         print('I am unable to see it')
#         sleep(0.5)

def mergesort(arr):
    n = len(arr)
    tmp_arr = [[0,0] for _ in range(n)]
    mergesort_algo(arr, tmp_arr, 0, n-1)
    return arr

def mergesort_algo(arr, tmp_arr, left, right):
    if left < right:
        mid = (left+right) //2
        mergesort_algo(arr, tmp_arr, left, mid)
        mergesort_algo(arr, tmp_arr, mid+1, right)
        merge(arr, tmp_arr, left, mid, right)

def merge(t, tmp, l, mid, r):
    i = k = l
    j = mid+1
    while i <= mid and j <= r:
        if t[i][0] <= t[j][0]:
            tmp[k] = t[i]
            i+=1
        else:
            tmp[k] = t[j]
            j += 1
        k+= 1
    while i<= mid:
        tmp[k] = t[i]
        k += 1
        i += 1
    while j <= r:
        tmp[k] = t[j]
        j+=1
        k+=1
    for q in range(l, r + 1):
        t[q] = tmp[q]

T = [4, 12, 5, 2, 19, 3]
for i in range(len(T)):
    T[i] = (T[i], i)
print(T)
x = mergesort(T)
print(x)