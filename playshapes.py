from xyz.supercoders.geometry.square import Square
from xyz.supercoders.geometry.rectangle import Rectangle
from shapestats import Shapestats

s = Square(side=5)

# print(s.area())
# print(s.perimeter())

Shapestats.calcstats(s)

r = Rectangle(length=6, breadth=3)

Shapestats.calcstats(r)