from xyz.supercoders.geometry.shape import Shape

class Shapestats:
  def calcstats(shape):
    if isinstance(shape, Shape):
      print('Area is {0}'.format(shape.area()))
      print('Perimeter is {0}'.format(shape.perimeter()))
    else:
      print('Pass in something which is Shape')