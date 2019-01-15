nos = [5, 6, 3, 10, 9, 3, 4, 6]

'''evens = []
for n in nos:
  if not n % 2:
    evens.append(n)

print(evens)'''

# filtering operation
# new list -> existing list

# for comprehensions
evens = [n for n in nos if not n % 2]
print(evens)

oddsgreater5 = [n for n in nos if n % 2 and n > 5]
print(oddsgreater5)

'''squares = []
for n in nos:
  squares.append(n ** 2)

print(squares)'''

# mapping operation
# new list -> existing list
squares = [n ** 2 for n in nos]
print(squares)
