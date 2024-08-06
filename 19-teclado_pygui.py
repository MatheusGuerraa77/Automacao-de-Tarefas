import pyautogui
import time

# pyautogui.press('winleft')
# time.sleep(1)
# pyautogui.write('calculadora')
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'shift', 'esc')
time.sleep(1)
with pyautogui.hold('winleft'):
    pyautogui.press('left')
    
time.sleep(2)
pyautogui.click()
time.sleep(2)
with pyautogui.hold('winleft'):
    pyautogui.press('right')