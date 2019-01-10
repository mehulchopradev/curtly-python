n = int(input('Enter n : '))

# i = 0

# while loop

'''while i <= n:
  if not i % 2:
    print(i)
  i += 1'''

# for loop
# for loop needs a sequence of values on which it will move
# for loop if given a sequence of 10 values will move its block 10 times
# for loop if given a sequence of 3 values will move its block 3 times

# sequence - 0 to n
# 0 - 20 (0, 1, 2, .... 20)
# range(0, n) - (0, 1, 2, ... n - 1)
# range(0, n + 1) - (0, 1, 2, ... n)

for v in range(0, n + 1):
  if not v % 2:
    print(v)
