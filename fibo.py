# n - 8
# 0 1 1 2 3 5 8 13
'''
  a b c
    a b c
      a b c
'''

n = int(input('Enter n : '))

def getfibo(n):
  result = ''
  a, b = 0, 1
  result += str(a) + ' ' + str(b) + ' '

  for v in range(1, n - 1):
    c = a + b
    result += str(c) + ' '
    a, b = b, c
  return result

print(getfibo(n))

'''a, b = 0, 1
print(a)
print(b)'''

'''i = 1

while i <= n-2:
  c = a + b
  print(c)
  a, b = b, c
  i += 1'''

# sequence
# range(1, n - 2 + 1) - (1, 2, 3, 4, 5, 6)
# range(1, n - 1)

'''for v in range(1, n - 1):
  c = a + b
  print(c)
  a, b = b, c'''

# print(c) # this will work as c is created in the module scope
# but dangerous
# if the for loop does not execute even once, the variable c will not be created