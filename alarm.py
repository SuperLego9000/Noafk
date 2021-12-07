import pyautogui as gui
import time
wait=time.sleep

from playsound import playsound
import threading

noisy=False
class alarm:
    noisy=False
    def stop():
        global noisy
        noisy=False
    def play():
        global noisy
        noisy=True
    def loop():
        while True:
            if noisy:
                playsound('P:/ROBLOX/Noafk/alarm.mp3')
        pass
    threading.Thread(target=loop).start()
while True:
    showgui=True
    while showgui:
        what=gui.confirm("you about to afk kick","Antiafk",["mute","start"])
        if what=="mute":
            alarm.stop()
        elif what=="start":
            alarm.stop()
            showgui=False
    wait(15*60)
    alarm.play()