#!/usr/bin/python
import spi
from time import sleep

SLEEPTIME=2

status = spi.openSPI(speed=5000000)
print "SPI configuration = ", status
# print "PY: initialising SPI mode, reading data, reading length . . . \n"

# How many total pixels?
pixels = 400

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
d = display(400)

while 1:
   d.setall(0, 255, 0)
   d.update()
   sleep(1)
   d.setall(255, 0, 0)
   d.update()
   sleep(1)
   d.clear()
   d.update()
   sleep(1)
