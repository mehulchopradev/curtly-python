# custom exception classes
class MinimumBalanceError(Exception):

  def __init__(self, message):
    super().__init__(message)