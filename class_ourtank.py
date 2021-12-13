class ourtank():
  def __init__(self,leftborder,topborder):   #Our tank coordinates
    self.direction = 'U'                     #Up Down Left Right
    self.pictures = {                        #load pictures
      'U':pygame.image.load(''),
      'D':,
      'L':,
      'R':,
      
    }
    self.picture = self.pictures[self.direction]
