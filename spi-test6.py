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

d = display(425)

d.clear()
d.update()

while 1:
  for level in range(5, 255, 20):
   d.setall(level,0,0)
   d.update()
   sleep(.25)
   d.setall(level,0,0)
   d.update()
   sleep(.005)
   d.setall(0,0,level)
   d.update()
   sleep(.25)

  for level in range(255, 10, -20):
   d.setall(level,0,0)
   d.update()
   sleep(.25)
   d.setall(level,0,0)
   d.update()
   sleep(.005)
   d.setall(0,0,level)
   d.update()
   sleep(.25)

if(true):
   for light in range(0, pixels, 2):
     d.set(light, 0, 0, 255) 
     d.set(light+1, 0, 0, 255)
     d.update()
   for light in range(0, pixels, 2):
     d.set(light, 0, 255, 0) 
     d.set(light+1, 0, 255, 0)
     d.update()
   for light in range(0, pixels, 2):
     d.set(light, 255, 0, 0) 
     d.set(light+1, 255, 0, 0)
     d.update()
   #sleep(1)
   #d.clear()
   #d.update()
   
