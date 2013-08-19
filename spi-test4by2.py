#!/usr/bin/python
import spi
from time import sleep
import random, time

width = 26
height = 16
thresh = 100  # charge threshold
charge = 1    # charging rate
sync = 13     # boost given to neighbors
rate = 20     # frames per sec

status = spi.openSPI(speed=5000000)
print "SPI configuration = ", status
# print "PY: initialising SPI mode, reading data, reading length . . . \n"

pixels = 424

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
   def set2d(self, x, y, rv, gv, bv):
      if y & 1:
         off = y * 26 + x
      else:
         off = y * 26 + (25 - x)
      self.set(off, rv, gv, bv)
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

d = display(424)

# how we display/fade
bright = 10
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

def push(x, y):
    if 0 <= x < width and 0 <= y < height:
        if state[y][x] > thresh * .8:
            state[y][x] += sync

while 1:
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
                push(x, y-1)
                push(x, y+1)
                push(x-1, y)
                push(x+1, y)

            else:
                # charge up
                state[y][x] += charge
                # blank/fade
                if screen[y][x] > 0:
                    screen[y][x] -= 1

    # draw screen
    for y in range(height):
        for x in range(width):
            d.set2d(x, y, screen[y][x]* 255/bright, 0, 0)
    d.update()

    time.sleep(1.0/rate)

SLEEPTIME=2
#At the beginning of the program open up the SPI port.
#this is port /dev/spidevX.Y
#Being called as as spi.SPI(X,Y)
#a = spi.SPI(0,0)


#spi.initialize()

def chase(red, green, blue):
  for light in range(0, pixels, 2):
     d.set(light, red, green, blue)
     #print("Setting LED #", light, red, green, blue)
     if(light != pixels):
       light = light + 1
       d.set(light, red, green, blue)
#     if(light != pixels):
#       light = light + 1
#       d.set(light, red, green, blue)
     #print("Setting LED #", light, red, green, blue)
     d.update()
     sleep(.02)

d.clear()
d.update()

while 1:
   for y in xrange(16):
      d.set2d(10, y, 0, 15 * y, 0)
   d.update()
