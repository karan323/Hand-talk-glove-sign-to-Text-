import board
import busio
import time
import os
import csv
import time
import board
import busio
import random
import math
from itertools import count

import matplotlib.pyplot as plt

import RPi.GPIO as GPIO
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg ,NavigationToolbar2Tk
#from matplotlib.figure import Fi
#import pandas as pd

with open('zsensordata.csv' , 'w+' , newline = '') as zfile:
    fieldnames = ['Sensor0', 'Sensor1', 'Sensor2', 'Sensor3']
    writer = csv.DictWriter(zfile, fieldnames=fieldnames)
    writer.writeheader()

i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)

i = 0

while i <= 100:
    chan0 = AnalogIn(ads, ADS.P0)
    chan1 = AnalogIn(ads, ADS.P1)
    chan2 = AnalogIn(ads, ADS.P2)
    chan3 = AnalogIn(ads, ADS.P3)
    print ( chan0.value )
    print ( chan1.value )
    print ( chan2.value )
    print ( chan3.value )
    fieldnames = ['Sensor0', 'Sensor1', 'Sensor2', 'Sensor3']
    i = i + 1
    with open('zsensordata.csv' , 'a' , newline = '') as zfile:
      writer = csv.DictWriter(zfile, fieldnames=fieldnames)
      writer.writerow({'Sensor0': chan0.value , 'Sensor1': chan1.value , 'Sensor2': chan2.value , 'Sensor3': chan3.value})
     
