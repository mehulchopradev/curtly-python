# module 'series' has reusable library kind of functions

def get_fiboseries(n):
  result = ''
  a, b = 0, 1
  result += str(a) + ' ' + str(b) + ' '

  for v in range(1, n - 1):
    c = a + b
    result += str(c) + ' '
    a, b = b, c
  return result

def get_even_series(n):
  result = ''
  for ele in range(0, n + 1, 2):
    result += str(ele) + ' '
  return result

# print(__name__) # magic variable
# when u run the module directly -> '__main__'
# when run using import from other module -> 'xyz.supercoders.lib.series'

if __name__ == '__main__':
  n = int(input('Heyy enter n : '))
  print(get_fiboseries(n))
  print(get_even_series(n))