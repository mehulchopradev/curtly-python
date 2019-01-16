# 0 to n arguments
def mysum(*args):
  # print(args)
  # print(type(args)) # tuple
  sum = 0
  for arg in args:
    sum += arg
  return sum

# positional arguments packing
print(mysum())
print(mysum(4))
print(mysum(5, 3, 4, 6))
print(mysum(5, 6, 7, 8, 2, 3, 4))


def area(length, breadth):
  return length * breadth

# positional arguments unpacked
stats = (5, 3)
# print(area(stats[0], stats[1]))
print(area(*stats))


# keyword argument packing
def perimeter(**stats):
  # return 2 * (length + breadth)
  # print(stats)
  # print(type(stats)) # dict
  return 2 * (stats['length'] + stats['breadth'])  

# print(perimeter(5, 3))
print(perimeter(length=5, breadth=3))
print(perimeter(breadth=3, length=5))
# print(perimeter(l=4, b=3)) # will not work


# keyword arguments unpacking
stats = {'breadth': 4, 'length': 8}
# print(area(stats['length'], stats['breadth']))
print(area(**stats))