#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO
import urllib.request

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

url = "https://flushedtolearn.herokuapp.com/media/online_song.mp3"
urllib.request.urlretrieve(url, "song.mp3")
i = 0
while True:
        if (GPIO.input(23) == False):
                urllib.request.urlretrieve(url, "song.mp3")
                
                print("playing song", i)
        i += 1
        sleep(0.1);
