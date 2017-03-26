#!/usr/bin/env python

import os
from time import sleep

import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

url = "https://flushedtolearn.herokuapp.com/media/online_song.mp3"

while True:
	if (GPIO.input(23) == False):
		os.system('mpg123 -q HappyClip.mp3 &')
	if (GPIO.input(24) == False):
		os.system('mpg123 -q IWillSurvive_Clip2.mp3 &')
	if (GPIO.input(25) == False):
		os.system('mpg123 -q SoLongFarewell.mp3 &')
	sleep(0.1);
