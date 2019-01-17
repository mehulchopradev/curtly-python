def abc():
  a = 5 # scope will abc
  b = 4

  def pqr(): # scope will abc
    print('PQR')
    print(a) # pqr() can access the enclosing function variables

    b = 10 # scope will pqr
    print(b) # 10
  
  pqr()
  print(b) # 4

abc()

# pqr() # will not work

# fun -> function object
# scope -> module
def fun():
  print('Fun')

# xyz -> function object
# scope -> module
def xyz(f):
  # f -> fun function object
  # scope f -> xyz
  f()

xyz(fun) # to pass a function as an argument to another function


def mno():
  print('Mno called')
  y = 3 # y -> scope -> mno -> and always accessible in ytd() even when mno() has returned
  z = 2

  def ytd(x): # ytd -> scope -> mno
    # closures
    print((x ** 2) + y)

  return ytd # to return a function from another function

func = mno()
func(5) # actually calling the ytd function defined inside mno