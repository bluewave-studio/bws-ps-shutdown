#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import time

waiting = True

def debounce(channel, state, count, attemptPeriod):
    attempts = 0
    
    while attempts < count:
        if GPIO.input(channel) != state:
            return False
        else:
            attempts += 1
            time.sleep(attemptPeriod / 1000)
        
    return True;

def onEventDetected(channel):
    state = 1
    count = 5
    attemptPeriod = 250
    
    if debounce(channel, state, count, attemptPeriod) == True:
        subprocess.call(['shutdown', '-h', 'now'], shell=False)
        global waiting
        waiting = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(3, GPIO.RISING, callback=onEventDetected)

while waiting:
    time.sleep(0.5)