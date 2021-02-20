import pyautogui
import time


def delay(time_delay):
    time.sleep(time_delay)

# print(pyautogui.size())

# pyautogui.moveTo(100, 100, duration = 1)
# pyautogui.moveRel(0, 20, duration = 1)

print(pyautogui.position())

# pyautogui.click(pyautogui.position())
for r in range(100):
    delay(10)
    pyautogui.click(1766, 785)
    pyautogui.typewrite("Modi Murdabad Modi Murdabad Modi Murdabad Modi Murdabad Modi Murdabad Modi Murdabad Modi Murdabad ")

    # pyautogui.typewrite("Jai Kisan Jai Kisan God please take care of the farmers who are killed by the police. Ek Ek laathi ka hisab hoga")
    pyautogui.click(1766, 827)

