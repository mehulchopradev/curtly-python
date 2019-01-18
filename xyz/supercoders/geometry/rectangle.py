from xyz.supercoders.geometry.shape import Shape

class Rectangle(Shape):
  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth

  def arearect(self):
    return self.length * self.breadth

  def peri(self):
    return 2 * (self.length + self.breadth)