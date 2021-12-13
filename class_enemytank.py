import time
import random
import pygame

class enemytank(tank):
  def__init__(self,left,top,speed):
    self.pictures = {
      'U': pygame.image.load('')'
      'D': pygame.image.load('')'
      'L': pygame.image.load('')'
      'R': pygame.image.load('')'
    }
    self.direction = 'D'
    self.picture = self.pictures[self.direction]
    self.rect = self.get_rect()