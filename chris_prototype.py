#Chris prototype setup - started 09 Sep 2017 Dallas, TX
#Verdure Systems Inc.
#Hardware Sparkfun BME280 Breakout

import time
import RPi.GPIO as GPIO
import logging
import Adafruit_BME280 

#set GPIO using 'board' numbering
GPIO.setmode(GPIO.board)
