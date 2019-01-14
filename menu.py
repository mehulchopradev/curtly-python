'''
1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Please enter ur choice : 1

Enter n : 8
0 1 1 2 3 5 8 13

1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Please enter ur choice : 2

Enter n : 10
0 2 4 6 8 10

1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Please enter ur choice : 3

Enter n : 5
It is odd

1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Please enter ur choice : 4
'''

# import series
from xyz.supercoders.lib.series import get_even_series, get_fiboseries as fiboseries
import math
import xyz.supercoders.lib.math

def get_fiboseries(n):
  return 'Bla Bla ' + str(n)

while True:
  print('1. Fibo Series\n2. Even Series\n3. Even or Odd\n4. Factorial\n5. Exit')
  choice = int(input('Please enter ur choice : '))

  if choice == 1 or choice == 2 or choice == 3 or choice == 4:
    n = int(input('Enter n : '))
  
  if choice == 1:
    # fiboseries for n
    print(fiboseries(n))
  elif choice == 2:
    # even series for n
    print(get_even_series(n))
  elif choice == 3:
    # even or odd for n
    print(xyz.supercoders.lib.math.evenOdd(n))
  elif choice == 4:
    print(math.factorial(n))
  else:
    break
