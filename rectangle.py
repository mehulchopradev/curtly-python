def perimeter(length, breadth):
  return 2 * (length + breadth)

# scope - module (file)
l = float(input('Enter length : '))
b = float(input('Enter breadth : '))

# str -> float
# '3.4' -> 3.4
# '2.1' -> 2.1

peri = perimeter(l, b)
print(peri)

def area():
  # refers the module scoped variable l and b
  # but consider avoiding this pattern
  # rather pass l and b as parameters to the function
  return l * b

def fun():
  l = 10 # local to the function fun
  b = 9 # local to the function fun

  print(l) # 10
  print(b) # 9

print(area())
fun()

print(l) # input
print(b) # input

# function and file (module) create a scope