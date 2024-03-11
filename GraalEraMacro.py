import pyautogui
import time
import keyboard
import sys

def StartMining(x,y):
    
    timeMining = 45
    start_time = time.time()
    pyautogui.moveTo(x,y,duration=1)
    while(time.time() - start_time) < timeMining:
        if(keyboard.is_pressed('q')):
            sys.exit()
        pyautogui.click(x,y,duration = 1.2)


time.sleep(2)
def StartProgram():
    while True:
        if(keyboard.is_pressed('q')):
            break
        else:
            StartMining(952,919) #Update the X and Y coordinated based on your requirements
            
            StartMining(890,852)
StartProgram()
