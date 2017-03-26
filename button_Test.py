#!/usr/bin/env python

import os
import pygame

from time import sleep

import RPi.GPIO as GPIO
import urllib.request

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

url = "https://s3.amazonaws.com/flushedsongsbucket/online_song.mp3"
urllib.request.urlretrieve(url, "song.mp3")
pygame.mixer.init()
i = 0
while True:
        if (GPIO.input(23) == False):
                urllib.request.urlretrieve(url, "song.mp3")
                print("playing song", i)
                os.system('omxplayer song.mp3')
                #os.system('omxplayer song.mp3')
                pygame.mixer.music.load("song.mp3")
                pygame.mixer.music.play()
               
        i += 1
        sleep(0.1);
