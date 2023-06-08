import pyautogui as p
from time import sleep
from os import system 

for i in range(4,0,-1):
    print(i)
    sleep(1)
    
while(True): 
    sleep(0.1)
    p.typewrite("This is an automated text")
    p.press("enter")
    sleep(0.1)




