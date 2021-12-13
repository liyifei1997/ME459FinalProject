class ourtank():
  def __init__(self,leftborder,topborder):   #Our tank coordinates
    self.direction = 'U' #Up
    self.pictures = {
      'U':,
      'D':,
      'L':,
      'R':,
      
    }
    self.picture = self.pictures[self.direction]
