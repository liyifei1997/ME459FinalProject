import pygame, time, random
import self as self

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
        MainGame.TANK_P1=Tank(500,500)
        while True:
            pygame.display.update()
            MainGame.window.fill(color_display)

            MainGame.window.blit(self.Text2("user manual"), (1400, 5))
            self.getevent()
            MainGame.window.blit(self.Text1("left 5 enermy tank"), (5, 5))
            MainGame.TANK_P1.display()
            if MainGame.TANK_P1 and not MainGame.Tank_p1.stop
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
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_DOWN or  pygame.K_DOWN
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


class Tank():
    def __init__(self,left,top):
        self.images = {'U': pygame.image.load(),'D':pygame.image.load(),'L':pygame.image.load(),'R':pygame.image.load()}
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect.left = left
        self.rect.top = top
        self.speed = 5
        self.stop =True
    def move(self):
        if self.direction == 'L'
            if self.rect.left>0
                self.rect.left = self.rect.left - self.speed
        elif self.direction == 'R'
            if self.rect.left+self.rect.height< MainGame.SCREEN_WIDTH
                self.rect.left = self.rect.left + self.speed
        elif self.direction == 'U'
            if self.rect.top>0
                self.rect.top = self.rect.top - self.speed
        elif self.direction == 'D'
            if self.rect.top+self.rect.height < MainGame.SCREEN_HEIGHT
                self.rect.top = self.rect.top + self.speed
    def fire(self):
        pass
    def display(self):
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)



MainGame().startgame()
