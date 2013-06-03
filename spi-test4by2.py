#!/usr/bin/python


# Python example for SPI bus, written by Brian Hensley
#This script will take any amount of Hex values and determine
#the length and then transfer the data as a string to the "spi" module

import spi
from time import sleep

SLEEPTIME=2
#At the beginning of the program open up the SPI port.
#this is port /dev/spidevX.Y
#Being called as as spi.SPI(X,Y)
#a = spi.SPI(0,0)


#spi.initialize()

status = spi.openSPI(speed=1000000)
print "SPI configuration = ", status
# print "PY: initialising SPI mode, reading data, reading length . . . \n"

pixels = 418

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

d = display(418)

def chase(red, green, blue):
  for light in range(0, pixels, 2):
     d.set(light, red, green, blue)
     #print("Setting LED #", light, red, green, blue)
     light = light + 1
     d.set(light, red, green, blue)
     #print("Setting LED #", light, red, green, blue)
     d.update()
     sleep(.0002)

d.clear()
d.update()

while 1:
  chase(255, 0, 0)
  #sleep()
  chase(0, 255, 0)
  #sleep(5)
  chase(0, 0, 255)
  #sleep(5)
