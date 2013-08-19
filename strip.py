import spi
from time import sleep
import random, time

width = 26
height = 16
pixels = 424

class display(object):
   def __init__(self, pixels=424):
       status = spi.openSPI(speed=5000000)
       self.pixels = pixels
       self.clear()
       self.width = width
       self.height = height
   def update(self):
       spi.transferrgb(self.red, self.green, self.blue)
   def set(self, pos, rv, gv, bv):
       '''set pixel at pos to rgb'''
       self.red[pos] = rv
       self.green[pos] = gv
       self.blue[pos] = bv
   def set2d(self, x, y, rv, gv, bv):
       if y & 1:
           off = y * 26 + (25 -x)
       else:
           off = y * 26 + (x)
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
