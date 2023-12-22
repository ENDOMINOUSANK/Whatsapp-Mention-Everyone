import pyautogui as pag
import time

peep = int(input("Total members in the group: "))
msg = input("Enter Message: ")
time.sleep(5)

pag.typewrite(msg)

for i in range(peep):
    time.sleep(0.2)
    pag.typewrite("@")
    time.sleep(0.2)
    pag.press('Down')
    time.sleep(0.5)
    pag.press('Enter')
    time.sleep(0.5)