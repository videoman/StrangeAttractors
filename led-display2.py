#!/usr/bin/python
import spi 
import random
import math
import time
from time import sleep

debug=1
random.seed(time.time())

SLEEPTIME=2

status = spi.openSPI(speed=5000000)
print "SPI configuration = ", status
# print "PY: initialising SPI mode, reading data, reading length . . . \n"

# How many total pixels?
pixels = 425

class display(object):
   def __init__(self, pixels):
      self.pixels = pixels
      self.clear()
   def update(self):
      spi.transferrgb(self.red, self.green, self.blue)
   def set(self, pos, rv, gv, bv):
      '''set pixel at pos to rgb'''
      self.red[pos] = rv
      self.green[pos] = gv
      self.blue[pos] = bv
   def setall(self, rv, gv, bv):
      '''set all pixels to rgb'''
      for pos in xrange(self.pixels):
         self.red[pos] = rv
         self.green[pos] = gv
         self.blue[pos] = bv
   def clear(self):
      '''clear all pixels to black'''
      self.red = [0] * pixels
      self.green = [0] * pixels
      self.blue = [0] * pixels

# How many pixels in the display do we have?
d = display(416)

#This is due to a bug.  
actpixels = 416
time_counter = 0

d.clear()
d.update()

time_counter = []

for p_temp in xrange(actpixels):
    time_counter.append(random.randrange(0,5))

width = 40
height = 20
thresh = 100  # charge threshold
charge = 1    # charging rate
sync = 13     # boost given to neighbors
rate = 10     # frames per sec

# how we display/fade
bright = 3
levels = ' .oO'

# build emptyarrays
screen = []
state = []
for y in range(height):
    screen.append([0] * width)
    state.append([0] * width)

# set all fireflies to a random state
for x in range(width):
    for y in range(height):
        state[y][x] = random.randint(0, thresh)

while 1:
    d.setall(255,255,255)
    d.update()
    # update state
    for x in range(width):
        for y in range(height):
            # fully charged?
            if state[y][x] > thresh:
                # flash on screen
                screen[y][x] = bright

                # lose all charge
                state[y][x] = 0

                # speed up nearest four neighbors
                if y > 0:
                    state[y-1][x] += sync
                if y < height - 1:
                    state[y+1][x] += sync
                if x > 0:
                    state[y][x-1] += sync
                if x < width - 1:
                    state[y][x+1] += sync
            else:
                # charge up
                state[y][x] += charge
                # blank/fade
                if screen[y][x] > 0:
                    screen[y][x] -= 1

    # draw screen
    #print '-' * width * 2
    #for y in range(height):
        #for x in range(width):
            #print levels[screen[y][x]],
        #print
    #print '-' * width * 2

    time.sleep(1.0/rate)
