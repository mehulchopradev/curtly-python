# all python classes implicitly inherit from the object class
class CollegeUser(object):

  def __init__(self, name, gender, mobilenos):
    self.name = name
    self.gender = gender

    if isinstance(mobilenos, list):
      self.mobilenos = mobilenos
    else:
      #TODO: Ideally should throw an error
      self.mobilenos = []

  # like the get_gender()
  @property
  def gender(self):
    return self.__gender

  # like the set_gender()
  @gender.setter
  def gender(self, gender):
    if gender == 'm' or gender == 'f':
      self.__gender = gender
    else:
      # TODO: Rather throw an error
      self.__gender = None

  def getdetails(self):
    str1 = 'Name -> {0}\nGender -> {1}\n'.format(self.name, self.gender)

    str2 = ''
    if self.mobilenos:
      for mobile in self.mobilenos:
        str2 += mobile + '\n'
    else:
      str2 = 'No Contact Number\n'

    return str1 + str2

  def __str__(self):
    return self.name