import os
import subprocess
import time
import datetime

enabledTimeRange = [(7, 10), (19, 22), (23, 24)]
check_period_mins = 10

def monitorOn():
    os.system("tvservice -p")

def monitorOff():
    os.system("tvservice -o")

def shouldMonitorBeOn():
    currentHour = datetime.datetime.now().hour
    shouldBeOn = False
    for timeRange in enabledTimeRange:
        shouldBeOn = shouldBeOn or (currentHour >= timeRange[0] and currentHour <= timeRange[1])
    return shouldBeOn

while True:
    if(shouldMonitorBeOn()):
        monitorOn()
    else:
        monitorOff()
    time.sleep(60 * check_period_mins)
