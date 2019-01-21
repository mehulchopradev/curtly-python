from traceback import print_exc

'''print('Program started')

n = int(input('Enter n : '))
if n % 2:
  print('Odd')
else:
  print('Even')

print('Program ends')'''

# Python env -> play_input -> int('good') -> ValueError -> play_input -> Python env
# Errors at runtime, premature returns from their context
# Errors - Exceptions


print('Program started')

# exception (error) handling
# a single try block can have multiple except blocks
# a single try - except block can even have an else block
try:
  n = int(input('Enter n : '))
except ValueError:
  # only exception (error) objects can be thrown and caught
  # print('Please enter numeric value')
  print_exc()
except Exception:
  # catch all exception block (in general avoid them!)
  print_exc()
else:
  # will execute when there is no exception (error) thrown in the corresponding try block
  if n % 2:
    print('Odd')
  else:
    print('Even')

print('Program ends')

# Python env -> play_input -> int('good') -> ValueError -> play_input
