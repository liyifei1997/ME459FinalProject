import time
import random
import pygame


color_display = pygame.Color(0, 0, 0)
color_text = pygame.Color(255, 0, 0)


class MainGame():
    # create the window of the game
    window = None
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900
    # create our tank
    TANK_P1 = None
    # TANK_P1.stop = True
    # TANK_P1.live = True
    # create enemy's tank
    EnemyTank_list = []
    # create amount of enemy's tank
    EnemyTank_count = 5
    # list to store our tank's ammo
    Bullet_list = []
    # list to store enemy's tank's ammo
    Enemy_bullet_list = []
    # list to store the effect of the explode
    Explode_list = []
    # list of wall
    Wall_list = []

    def __init__(self):
        pass

    def startgame(self, Tank_p1=None):
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        pygame.display.set_caption("bettle tank")
        MainGame.TANK_P1=tank(500,500)
        while True:
            pygame.display.update()
            MainGame.window.fill(color_display)

            MainGame.window.blit(self.Text2("user manual"), (1400, 5))
            self.getevent()
            MainGame.window.blit(self.Text1("left 5 enermy tank"), (5, 5))
            MainGame.TANK_P1.display()
            if MainGame.TANK_P1 and not MainGame.TANK_P1 == True:
                MainGame.TANK_P1.move()
            pygame.display.update()
            time.sleep(0.02)

    def getevent(self):
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                self.endgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("go left")
                    MainGame.TANK_P1.direction = 'L'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    print("go right")
                    MainGame.TANK_P1.direction = 'R'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_UP:
                    print("go up")
                    MainGame.TANK_P1.direction = 'U'
                    MainGame.TANK_P1.stop = False

                elif event.key == pygame.K_DOWN:
                    print("go down")
                    MainGame.TANK_P1.direction = 'D'
                    MainGame.TANK_P1.stop = False

                elif event.key == pygame.K_SPACE:
                    pass
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_DOWN or  pygame.K_DOWN:
                MainGame.TANK_P1.stop = True
    def Text1(self, word):
        pygame.font.init()
        # textlist = pygame.font.get_fonts()
        text = pygame.font.SysFont('arial', 20)
        textsurf1 = text.render(word, True, color_text)
        return textsurf1

    def Text2(self, word):
        pygame.font.init()
        # textlist = pygame.font.get_fonts()
        text = pygame.font.SysFont('arial', 20)
        textsurf2 = text.render(word, True, color_text)
        return textsurf2

    def endgame(self):
        print("Thanks for Playing")
        # end the game
        exit()


class tank():
    def __init__(self, left, top):  # Our tank coordinates
        self.direction = 'U'  # Up Down Left Right
        self.pictures = {  # load pictures
            'U': pygame.image.load('img/ourU.jpg'),
            'D': pygame.image.load('img/ourD.jpg'),
            'L': pygame.image.load('img/ourL.jpg'),
            'R': pygame.image.load('img/ourR.jpg'),
        }
        self.picture = self.pictures[self.direction]
        self.rect = self.picture.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 5
        self.stop =True
    def move(self):
        if self.direction == 'L':
            if self.rect.left>0:
                self.rect.left = self.rect.left - self.speed
        elif self.direction == 'R':
            if self.rect.left+self.rect.height< MainGame.SCREEN_WIDTH:
                self.rect.left = self.rect.left + self.speed
        elif self.direction == 'U':
            if self.rect.top>0:
                self.rect.top = self.rect.top - self.speed
        elif self.direction == 'D':
            if self.rect.top+self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top = self.rect.top + self.speed
    def fire(self):
        pass
    def display(self):
        self.picture = self.pictures[self.direction]
        MainGame.window.blit(self.picture,self.rect)



class enemytank(tank):
  def __init__(self,left,top,speed):
    self.pictures = {
      'U': pygame.image.load('img/enemyU.jpg'),
      'D': pygame.image.load('img/enemyD.jpg'),
      'L': pygame.image.load('img/enemyL.jpg'),
      'R': pygame.image.load('img/enemyR.jpg'),
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

import time
import random
import pygame

class ourtank(tank):
  def __init__(self,left,top):
    super(ourtank,self).__init__(left,top)

import time
import random
import pygame

class ammo():
  def __init__(self,tank):
    self.live = True
    self.picture = pygame.image.load('img/ammo.gif')
    self.direction = tank.direction
    if self.direction == 'U':
      self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
      self.rect.top = tank.rect.top - self.rect.top
    elif self.direction == 'D':
      self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
      self.rect.top = tank.rect.top + tank.rect.height
    elif self.direction == 'L':
      self.rect.left = tank.rect.left - self.rect.width/2 - self.rect.width/2
      self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
    elif self.direction == 'R':
      self.rect.left = tank.rect.left + tank.rect.width
      self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
    self.rect = self.picture.get_rect()
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
    MainGame.window.blit(self.picture,self.rect)
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

import time
import random
import pygame

class explode():
  def __init__(self,tank):
    self.rect = tank.rect
    self.step = 0
    self.pictures = [
      pygame.image.load('img/explode.gif')
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

class steel():
  def __init__(self,left,top):
    self.picture = pygame.image.load('img/steels.jpg')
    self.rect = self.picture.get_rect()
    self.rect.left = left
    self.rect.top = top
    self.live = True
    self.hp = 3
  def displaysteel(self):
    MainGame.window.blit(self.picture,self.rect)





MainGame().startgame()
