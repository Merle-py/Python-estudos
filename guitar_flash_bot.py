import pyautogui
import keyboard
from time import sleep

alturaTela, larguraTela = pyautogui.size()
alturaTela, larguraTela = (1920,1080)

#cores das notas
verde = (0,152,0)
vermelho = (255,0,0)
amarelo = (247,247,79)
azul = (0,152,255)
laranja = (255,101,0)

while not keyboard.is_pressed('1'):
    pressionar_teclas = []
    
    if(pyautogui.pixelMatchesColor(742,900,verde)):
        pressionar_teclas.append('a')
    if(pyautogui.pixelMatchesColor(834,900,vermelho)):
        pressionar_teclas.append('s')
    if(pyautogui.pixelMatchesColor(947,900,amarelo)):
        pressionar_teclas.append('j')
    if(pyautogui.pixelMatchesColor(1051,900,azul)):
        pressionar_teclas.append('k')
    if(pyautogui.pixelMatchesColor(1158,900,laranja)):
        pressionar_teclas.append('l')

    for tecla in pressionar_teclas:
        pyautogui.keyDown(tecla)

    for tecla in pressionar_teclas:
        pyautogui.keyUp(tecla)

    sleep(0.01)