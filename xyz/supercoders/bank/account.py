from xyz.supercoders.bank.minbalerror import MinimumBalanceError
class Account:

  minbalance = 2000

  def __init__(self, accno, accname, acctype, accbalance):
    self.accno = accno
    self.accname = accname
    self.acctype = acctype
    self.accbalance = accbalance

  def deposit(self, depositamt):
    self.accbalance += depositamt
    return self.accbalance

  def withdraw(self, withdrawamt):
    '''
    withdraws the passed amount from the balance. Raises ValueError when the passed
    withdrawl amount is less than or 0. Raises MinimumBalanceError if the minumum 
    balance will not be able to be maintained after this withdrawl'''

    print('Withdrawl transaction starts...')

    try:
      if withdrawamt <= 0:
        raise ValueError('Withdrawl amount to be greater than 0')
      if self.accbalance - withdrawamt < Account.minbalance:
        # raise an error to whoever is ur caller
        raise MinimumBalanceError('Account balance going below {0}'.format(Account.minbalance))

      self.accbalance -= withdrawamt
      return self.accbalance
    finally:
      # will always execute irrespective of whether an error is raised or not raised in the
      # corresponding try block
      # try - finally
      # try - except - finally
      print('Withdrawl transaction ends.')