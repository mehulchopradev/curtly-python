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