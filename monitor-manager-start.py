import os
import subprocess
import time
import datetime

enabledTimeRange = [(7, 10), (19, 22), (23, 24)]
check_period_mins = 10

def monitorOn():
    os.system("tvservice -p")
    os.system("xset -display :0 s off -dpms")
    os.system("DISPLAY=:0 xdg-screensaver reset")

def monitorOff():
    os.system("tvservice -o")

def shouldMonitorBeOn():
    currentHour = datetime.datetime.now().hour
    shouldBeOn = False
    for timeRange in enabledTimeRange:
        shouldBeOn = shouldBeOn or (currentHour >= timeRange[0] and currentHour <= timeRange[1])
    return shouldBeOn

# Turn off dpms
os.system("xset -display :0 s off -dpms")
os.system("xset -display :0 s noblank")
os.system("xset -display :0 s noexpose")
os.system("xset -display :0 s 0")
os.system("DISPLAY=:0 xdg-screensaver reset")

while True:
    if(shouldMonitorBeOn()):
        monitorOn()
    else:
        monitorOff()
    time.sleep(60 * check_period_mins)
