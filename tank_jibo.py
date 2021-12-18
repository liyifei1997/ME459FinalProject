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
    enemytank_list = []
    # create amount of enemy's tank
    enemytank_count = 5
    # list to store our tank's ammo
    ammo_list = []
    # list to store enemy's tank's ammo
    enemyammo_list = []
    # list to store the effect of the explode
    explode_list = []
    # list of wall
    steel_list = []

    def startgame(self):
        pygame.display.init()
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        pygame.display.set_caption("bettle tank")
        self.enemytank()
        self.ourtank()
        self.createsteel()

        while True:
            pygame.display.update()
            MainGame.window.fill(color_display)

            MainGame.window.blit(self.Text2("user manual"), (1400, 5))
            self.getevent()
            MainGame.window.blit(self.Text1("left 5 enermy tank"), (5, 5))
            # to display our tank when it alive
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                MainGame.TANK_P1.displayTank()
            else:
                # delete our tank when it is eliminated
                del MainGame.TANK_P1
                MainGame.TANK_P1 = None
            # add enemy tanks
            self.showenemytank()
            # move out tank
            if MainGame.TANK_P1 and not MainGame.TANK_P1 == True:
                MainGame.TANK_P1.move()
            # when tanks hit wall
            MainGame.TANK_P1.hitsteel()
            # when tank hits tank
            MainGame.TANK_P1.hitenemytank()
            # show wall
            self.showsteel()
            # use our tank bullet list
            self.showbullet()
            # use enemy tank bullet list
            self.showenemyammo()
            # show exlodsion
            self.showexplodes()
            pygame.display.update()
            time.sleep(0.02)



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

    def ourtank(self):
        # 创建我方坦克
        MainGame.TANK_P1 = ourtank(400, 300)

    def enemytank(self):
        top = 100
        for i in range(MainGame.enemytank_count):
            # 控制坦克的移动速度
            speed = random.randint(3, 6)
            left = random.randint(1, 7)
            eTank = enemytank(left * 100, top, speed)
            MainGame.enemytank_list.append(eTank)
    def showourtank(self):
        pass

    def showenemytank(self):
        for eTank in MainGame.enemytank_list:
            if eTank.live:
                eTank.displayTank()
                # 敌方坦克移动方法
                eTank.randommove()
                # 调用敌方坦克与墙壁的碰撞方法
                eTank.hitsteel()
                # 调用敌方坦克碰撞到我方坦克的方法
                eTank.hitourtank()
                # 调用敌方坦克的射击
                eBullet = eTank.shot()
                if eBullet:
                    # 将子弹存储在敌方坦克子弹的列表
                    MainGame.enemyammo_list.append(eBullet)
            else:
                MainGame.enemytank_list.remove(eTank)

    def createsteel(self):
        for i in range(1, 7):
            steelwall = steel(120 * i, 240)
            MainGame.steel_list.append(steelwall)

    # 将墙壁粘贴在窗口中
    def showsteel(self):
        for steelwall in MainGame.steel_list:
            if steelwall.live:
                steelwall.displaysteel()
            else:
                MainGame.steel_list.remove(steelwall)

    # 将敌方坦克加入到窗口中


    # 将我方坦克子弹加入到窗口中
    def showbullet(self):
        for bullet in MainGame.ammo_list:
            if bullet.live == True:
                bullet.showammo()
                # 让子弹移动
                bullet.ammomove()
                # 调用我方子弹与敌方坦克的碰撞方法
                bullet.hitenemytank()
                # 调用判断我方子弹是否碰撞墙壁的方法
                bullet.hitsteel()
            else:
                MainGame.bullet_list.remove(bullet)

    # 将敌方坦克子弹加入到窗口中
    def showenemyammo(self):
        for eBullet in MainGame.enemyammo_list:
            if eBullet.live:
                eBullet.showammo()
                # 让子弹移动
                eBullet.ammomove()
                # 调用判断敌方子弹是否碰撞墙壁的方法
                eBullet.hitsteel()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    # 敌方坦克子弹打中我方坦克
                    eBullet.hitourtank()
            else:
                MainGame.enemyammo_list.remove(eBullet)

    def showexplodes(self):
        for explode in MainGame.explode_list:
            if explode.live:
                explode.showexplode()
            else:
                MainGame.wxplode_list.remove(explode)

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
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_DOWN or pygame.K_DOWN:
                MainGame.TANK_P1.stop = True

    def endgame(self):
        print("Thanks for Playing")
        # end the game
        exit()


class basicitem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class tank(basicitem):
    def __init__(self, left, top):  # Our tank coordinates
        self.direction = 'U'  # Up Down Left Right
        self.pictures = {  # load picturess
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
        self.step = 20
        self.live = True
        self.stop = True
        # record the old coordinates before moving
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    def move(self):
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left = self.rect.left - self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < MainGame.SCREEN_WIDTH:
                self.rect.left = self.rect.left + self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top = self.rect.top - self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top = self.rect.top + self.speed
        # make tank stay in original place

    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop

    def hitsteel(self):
        for steelwall in MainGame.steel_list:
            if pygame.sprite.collide_rect(steelwall, self):
                self.stay()

    def displayTank(self):
        # reset tank's image
        self.picture = self.pictures[self.direction]
        # show tank on window
        MainGame.window.blit(self.picture, self.rect)

    def display(self):
        self.picture = self.pictures[self.direction]
        MainGame.window.blit(self.picture, self.rect)


class ourtank(tank):
    def __init__(self, left, top):
        super(ourtank, self).__init__(left, top)

    # 新增我方坦克主动碰撞到敌方坦克的方法
    def hitenemytank(self):
        for eTank in MainGame.enemytank_list:
            if pygame.sprite.collide_rect(eTank, self):
                self.stay()


class enemytank(tank):
    def __init__(self, left, top, speed):
        super(enemytank, self).__init__(left, top)
        self.pictures = {
            "U": pygame.image.load('img/enemyU.jpg'),
            "D": pygame.image.load('img/enemyD.jpg'),
            "L": pygame.image.load('img/enemyL.jpg'),
            "R": pygame.image.load('img/enemyR.jpg'),
        }
        self.direction = self.randomdirection()
        self.picture = self.pictures[self.direction]
        self.rect = self.picture.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.stop = True
        self.step = 5

    def randomdirection(self):
        number = random.randint(1, 4)
        if number == 1:
            return 'U'
        elif number == 2:
            return 'D'
        elif number == 3:
            return 'L'
        elif number == 4:
            return 'R'

    def displayenemytank(self):
        super().displaytank()

        def randommove(self):
            if self.step <= 0:
                self.direction = self.randomdirection()
                self.step = 20
            else:
                self.move()
                self.step -= 1

    def randommove(self):
        if self.step <= 0:
            self.direction = self.randomdirection()
            self.step = 20
        else:
            self.move()
            self.step -= 1

    def shot(self):
        num = random.randint(1, 1000)
        if num <= 20:
            return ammo(self)

    def hitourtank(self):
        if MainGame.TANK_P1 and MainGame.TANK_P1.live:
            if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
                self.stay()


class ammo():
    def __init__(self, tank):
        self.speed = 8
        self.live = True
        self.picture = pygame.image.load('img/ammo.gif')
        self.direction = tank.direction
        self.rect = self.picture.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.top
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2



    def ammomove(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
                self.rect.left += self.speed
            else:
                self.live = False

    def showammo(self):
        MainGame.window.blit(self.picture, self.rect)

    def hitenemytank(self):
        for enemytank in MainGame.enemytank_list:
            if pygame.sprite.collide_rect(enemytank, self):
                explode = Explode(enemytank)
                MainGame.Expolde_list.append(explode)
                self.live = False
                eTank.live = False

    def hitourtank(self):
        if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
            explode = Explode(MainGame.TANK_P1)
            MainGame.Explode_list.append(explode)
            self.live = False
            MainGame.TANK_P1.live = False

    def hitsteel(self):
        for steelwall in MainGame.steel_list:
            if pygame.sprite.collide_rect(steelwall, self):
                self.live = False
                steelwall.hp -= 1
                if steelwall.hp <= 0:
                    steelwall.live = False


class explode():
    def __init__(self, tank):
        self.rect = tank.rect
        self.step = 0
        self.pictures = [
            pygame.image.load('img/explode.gif')
        ]
        self.picture = self.pictures[self.step]
        self.live = True

    def showexplode(self):
        if self.step < len(self.pictures):
            MainGame.window.blit(self.picture, self.rect)
            self.picture = self.pictures[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0


class steel():
    def __init__(self, left, top):
        self.picture = pygame.image.load('img/steels.jpg')
        self.rect = self.picture.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True
        self.hp = 3

    def displaysteel(self):
        MainGame.window.blit(self.picture, self.rect)


MainGame().startgame()
