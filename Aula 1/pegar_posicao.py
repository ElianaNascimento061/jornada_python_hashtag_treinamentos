import pyautogui
import time

time.sleep(5)
print (pyautogui.position()) #Pega a posição onde está o cursor do mouse
pyautogui.scroll(-200) #Scrolla a tela quando acabar o tempo