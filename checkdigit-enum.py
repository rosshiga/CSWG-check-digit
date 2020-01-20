import pyautogui 
import math
import time


def leadingZero(number):
    digits = int(math.log10(number))+1
    while digits < 5:
        number = "0" + str(number)
        digits += 1
    return number
pyautogui.PAUSE = 0.001
time.sleep(8)
for i in range(0, 10000): 
    x = leadingZero(i)
    print(x)
    pyautogui.typewrite(str(x))
    pyautogui.press('enter')


