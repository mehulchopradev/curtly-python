nos = [5, 6, 3, 4, 2, 1, 5, 6, 8, 9]

# filtering
'''def iseven(ele):
  return not ele % 2'''

'''nl = filter(iseven, nos)
for n in nl:
  print(n)'''

# preconditions
# function that is passed as an argument to another function, must have only one expression statement
# lambda functions

nl = filter(lambda ele: not ele % 2, nos)
'''for n in nl:
  print(n)'''

ol = filter(lambda ele: ele % 2 and ele > 5, nos)
'''for o in ol:
  print(o)'''

# mapping
sl = map(lambda ele: ele ** 2, nos)
for s in sl:
  print(s)

