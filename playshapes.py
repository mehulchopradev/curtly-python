from xyz.supercoders.geometry.square import Square
from xyz.supercoders.geometry.rectangle import Rectangle
from xyz.supercoders.geometry.shape import Shape
from shapestats import Shapestats

# ss = Shape() # cant instantiate (create objects) of abstract class with astract methods

s = Square(side=5)

# print(s.area())
# print(s.perimeter())

Shapestats.calcstats(s)

r = Rectangle(length=6, breadth=3)

Shapestats.calcstats(r)