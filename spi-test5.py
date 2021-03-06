#!/usr/bin/python


# Python example for SPI bus, written by Brian Hensley
#This script will take any amount of Hex values and determine
#the length and then transfer the data as a string to the "spi" module

import spi
from time import sleep

#At the beginning of the program open up the SPI port.
status = spi.openSPI(speed=5000000)
print "SPI configuration = ", status
# print "PY: initialising SPI mode, reading data, reading length . . . \n"

pixels = 416

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

d = display(416)

for i in range(6):
  d.setall(255, 0, 0)
  d.update()
  sleep(.1)
  d.clear()
  d.update()
  sleep(.1)

FADETIME=.04

while 1:
  sleep(.005)
  for bcolor in xrange(0, 90, 2):
     sleep(FADETIME)
     for rcolor in xrange(0, 255, 5):
       sleep(FADETIME)
       for gcolor in xrange(0, 255, 10):
         d.setall(rcolor, gcolor , bcolor)
         d.update()
         sleep(FADETIME)
     sleep(.02)
  for bcolor in xrange(255, 0, -2):
    sleep(FADETIME)
    for rcolor in xrange(255, 0, -2):
      sleep(FADETIME)
      for gcolor in xrange(255, 0, -2):
        d.setall(rcolor, gcolor , bcolor)
        d.update()
        sleep(FADETIME)
    sleep(.02)

