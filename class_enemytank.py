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
    self.direction = self.randomdirection()
    self.picture = self.pictures[self.direction]
    self.rect = self.get_rect()
    self.rect.left = left
    self.rect.top = top
    self.speed = speed
    self.stop = True
  def randomdirection(self):
    number = random.randint(1,4)
    if number == 1:
      self.direction = 'U'
    elif number ==2:
      self.direction = 'D'
    elif number ==3:
      self.direction = 'L'
    elif number ==4:
      self.direction = 'R'
  def displayenemytank(self):
    super().displaytank()
