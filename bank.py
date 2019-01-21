from xyz.supercoders.bank.account import Account
from xyz.supercoders.bank.minbalerror import MinimumBalanceError
from traceback import print_exc

a1 = Account(accno='234563245674', acctype='Savings', accbalance=9000, accname='mehul chopra')

print('Deposit')
print('Updated balance {0}'.format(a1.deposit(1000)))

print('Withdrawl')

try:
  ub = a1.withdraw(9000)
except ValueError:
  print_exc()
except MinimumBalanceError:
  print_exc()
else:
  print('Updated balance {0}'.format(ub))

print('Transactions ends')