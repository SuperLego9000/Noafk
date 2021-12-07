import pyautogui as gui
import time
wait=time.sleep

from playsound import playsound
import threading

what=gui.confirm("Method","Noafk",["Alarm","Full afk"])

if what=="Alarm":
    import alarm
elif what=="Full afk":
    import afk