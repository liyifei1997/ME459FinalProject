import time
import random
import pygame

class explode():
  def __init__(self,tank):
    self.rect = tank.rect
    self.step = 0
    self.pictures = [
      pygame.image.load('')
    ]
    self.picture = self.pictures[self.step]
    self.live = True
    
  def displayexplode(self):
    if self.step < len(self.pictures):
      MainGame.window.blit(self.picture,self.rect)
      self.picture = self.pictures[self.step]
      self.step += 1
    else:
      self.live = False
      self.step = 0
