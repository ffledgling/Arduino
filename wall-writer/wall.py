#!/usr/bin/env python

import serial
import time

# Motors doesn't seem to do the full 180, looks about 10-15 degree short, so we adjust our "center" accordingly.
X0 = 96
Y0 = 96

# Note: Our "baud rate" is limited to 9600. Every "command" we send is 3bytes, so
# we're limited to 9600/(3*8) = 400 commands a second, or one every 2.5ms
# We wait 20ms just to be on the safe side
# Addendum: Apparently the PWM cycle of our motor is also 20ms, so we can't go any faster than that anyway
# Addendum2: Our motor's top speed is 0.1s/60deg so there's not much point trying to go faster than that. 
SLP = 0.2 # Sleep for 0.1s between every movement

# Connect to Arduino over Serial console
ser = None

# We hard code our USB port ttys here, they may wary
try:
    ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
except serial.serialutil.SerialException:
    ser = serial.Serial('/dev/tty.usbmodem1421', 9600)

def center(): 
    ser.write(b'C' + bytes([X0, Y0]))

def point(x, y):
    # Adjust the positive and negative around to match the regular mathematical
    # grid (machine is just setup this way, it is what it is)
    print('C:', x, y)
    ser.write(b'C' + bytes([X0 - x, Y0 + y]))

def on():
    ser.write(b'H')

def off():
    ser.write(b'L')

# Function that attempts to draw a square
# This draws a filled square
def square():
    while True:
        for x in range(-20, 21,4):
            for y in range(-20, 21, 4):
                point(x, y)
                # Our "baud rate" is limited to 9600. Every "command" we send is 3bytes, so
                # we're limited to 9600/(3*8) = 400 commands a second, or one every 2.5ms
                # We wait 20ms just to be on the safe side

                time.sleep(0.01)

def lineimpl1(p1, p2):
    print("Drawing line with points:", p1, p2)
    point(p1[0], p1[1])
    on()
    time.sleep(SLP)
    point(p2[0], p2[1])
    time.sleep(SLP)
    off()

def lineimpl2(p1, p2):
    print("Drawing line with points:", p1, p2)
    point(p1[0], p1[1])
    time.sleep(SLP)
    point(int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2))
    time.sleep(SLP)
    point(p2[0], p2[1])

def line(p1, p2):
    lineimpl1(p1, p2)
    #lineimpl2(p1, p2)

def draw(shape, *args, **kwargs):
    while True:
        shape(*args, **kwargs)

# Lets try an empty one
def square2(size):
    point(-size,-size)
    time.sleep(SLP)
    point(-size,size)
    time.sleep(SLP)
    point(size,size)
    time.sleep(SLP)
    point(size,-size)
    time.sleep(SLP)
        
