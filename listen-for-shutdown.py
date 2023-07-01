#!/usr/bin/env python
# CONFIG
PIN = 3
HOLD_TIME = 1 #seconds

import RPi.GPIO as GPIO
import subprocess
from time import perf_counter


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)
while True:
    GPIO.wait_for_edge(PIN, GPIO.FALLING)
    start = perf_counter()
    while perf_counter()<start+HOLD_TIME:
        if GPIO.input(PIN) == GPIO.HIGH:
            break
    else:
        subprocess.call(['shutdown', '-h', 'now'], shell=False)
