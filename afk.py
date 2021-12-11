from rbxmove import rbxmove as rbx
from time import sleep as wait
from texts import texts
import random as r
from win32gui import GetWindowText, GetForegroundWindow
print("tab to roblox")
while True:
    if GetWindowText(GetForegroundWindow())=="Roblox":
        rbx.move(r.choice(['w','a','s','d']),r.randint(5, 9))#move asap so we lower afk chance
        print(texts.restart)
        rbx.countto(r.randint(3*60,5*60))#wait 3-5 minutes
        if GetWindowText(GetForegroundWindow())=="Roblox":#if we still in roblox
            rbx.move(r.choice(['w','a','s','d']),r.randint(5, 9))#move some
            rbx.game.reset()#try to reset
    else:
        print(texts.tab)