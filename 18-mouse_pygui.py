import pyautogui
import time

# 1 - Tamanho da Tela
print(pyautogui.size())

# 2 - Pegar a posição atual do cursor do mouse
print(pyautogui.position())
time.sleep(1.5)

# 3 - App para vê a posição do mouse no tempo real
# python
# from pyautogui import mouseInfo
# mouseInfo()

# 4 - Mover o cursor do mouse
pyautogui.moveTo(1804, 16, 1)
time.sleep(1.5)
pyautogui.click()

# 5 - realizando o scroll
time.sleep(1.5)
pyautogui.moveTo(1047, 840)
pyautogui.click()
time.sleep(1.5)
pyautogui.scroll(900)