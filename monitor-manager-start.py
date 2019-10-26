import os
import subprocess
import time
import datetime

enabledWeekdayTimeRange = [(7, 10)]
enabledWeekendTimeRange = [(9,11), (16, 19)]

check_period_mins = 9 # monitor times out after 10 mins

def monitorOn():
    os.system("tvservice -p")
    os.system("xset -display :0 s off -dpms")
    os.system("DISPLAY=:0 xdg-screensaver reset")

def monitorOff():
    os.system("tvservice -o")

def shouldMonitorBeOn():
    currentDateTime = datetime.datetime.now()
    currentHour = currentDateTime.hour
    isWeekday = currentDateTime.weekday() < 5
    enabledTimeRange = enabledWeekdayTimeRange if isWeekday else enabledWeekendTimeRange

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
