class ourtank():
  def __init__(self,leftborder,topborder):   #Our tank coordinates
    self.direction = 'U'                     #Up Down Left Right
    self.pictures = {                        #load pictures
      'U':pygame.image.load(''),
      'D':pygame.image.load(''),
      'L':pygame.image.load(''),
      'R':pygame.image.load(''),
      
    }
    self.picture = self.pictures[self.direction]
