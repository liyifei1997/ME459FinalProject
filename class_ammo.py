import time
import random
import pygame

class ammo():
  def __init__(self,tank):
    self.live = True
    self.picture = pygame.image.load('')
    self.direction = tank.direction
    if self.direction == 'U'
      self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
      self.rect.top = tank.rect.top - self.rect.top
    elif self.direction == 'D'
      self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
      self.rect.top = tank.rect.top + tank.rect.height
    elif self.direction == 'L'
      self.rect.left = tank.rect.left - self.rect.width/2 - self.rect.width/2
      self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
    elif self.direction == 'R'
      self.rect.left = tank.rect.left + tank.rect.width
      self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
    self.rect = self.image.get_rect()
    self.speed = 8
  def ammomove(self):
    if self.direction == 'U':
      if self.rect.top > 0:
        self.rect.top -= self.speed
      else:
        self.live = False
    elif self.direction == 'D':
      if self.rect.top < Maingame.SCREEN_HEIGHT - self.rect.height:
        self.rect.top += self.speed
      else:
        self.live = False
    elif self.direction == 'L':
      if self.rect.left > 0:
        self.rect.left -= self.speed
      else:
        self.live = False
    elif self.direction == 'R':
      if self.rect.left < Maingame.SCREEN_WIDTH - self.rect.width:
        self.rect.left += self.speed
      else:
        self.live = False
  def displayammo(self):
    MainGame.window.blit(self.image,self.rect)
  def hitenemytank(self):
    for enemytank in MainGame.EnemyTank_list:
      if pygame.sprite.collide_rect(enemytank,self):
        explode = Explode(enemytank)
        MainGame.Expolde_list.append(explode)
        self.live = False
        enemy.live = False
    def hitourtank(self):
      if pygame.sprite.collide_rect(self,MainGame.TANK_P1):
        explode = Explode(MainGame.TANK_P1)
        MainGame.Explode_list.append(explode)
        self.live = False
        MainGame.TANK_P1.live = False
  def hitsteel(self):
    for wall in MainGame.Wall_list:
      if pygame.sprite.collide_rect(wall,self):
        self.live = False
        wall.hp -= 1
        if wall.hp <= 0:
          wall.live = False
