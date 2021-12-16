class steel():
  def __init__(self,left,top):
    self.image = pygame.image.load('')
    self.rect = self.image.get_rect()
    self.rect.left = left
    self.rect.top = top
    self.live = True
    self.hp = 3
  def displaysteel(self):
    MainGame.window.blit(self.image,self.rect)
