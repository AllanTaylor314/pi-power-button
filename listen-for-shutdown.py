#!/usr/bin/env python
# CONFIG
PIN = 3
HOLD_TIME = 1000 # milliseconds

import RPi.GPIO as GPIO
import subprocess
from time import perf_counter_ns


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)
while True:
    GPIO.wait_for_edge(PIN, GPIO.FALLING)
    start = perf_counter_ns()
    while perf_counter_ns()<start+HOLD_TIME*1_000_000:
        if GPIO.input(PIN) == GPIO.HIGH:
            break
    else:
        subprocess.call(['shutdown', '-h', 'now'], shell=False)
