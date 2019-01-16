class Student:

  # class attributes
  count = 0

  def __init__(self, name, roll, gender, marks, mobilenos=[]):
    # constructor
    # configuring/adding attributes to the object
    self.name = name
    self.roll = roll
    self.gender = gender
    self.marks = marks

    if isinstance(mobilenos, list):
      self.mobilenos = mobilenos
    else:
      #TODO: Ideally should throw an error
      self.mobilenos = []

    Student.count += 1

  # object methods
  def getdetails(self):
    #str1 = 'Name : ' + self.name + '\nGender : ' + self.gender + '\nRoll : ' + str(self.roll) \
    #+ '\nMarks : ' + str(self.marks) + '\n'

    #str1 = 'Name : {0}\nGender : {1}\nRoll : {2}\nMarks : {3}\n'.format(self.name, self.gender, self.roll\
    #  , self.marks)

    str1 = 'Name : {name}\nGender: {gender}\nRoll: {roll}\nMarks: {marks}\n'.format(\
      name=self.name, roll=self.roll, gender=self.gender, marks=self.marks)

    str2 = ''
    if self.mobilenos:
      for mobile in self.mobilenos:
        str2 += mobile + '\n'
    else:
      str2 = 'No Contact Number'
    
    return str1 + str2

  def getgrade(self):
    marks = self.marks
    if marks > 100 or marks < 0:
      return 'I'
    elif marks >= 70:
      return 'A'
    elif marks >= 60:
      return 'B'
    elif marks >= 40:
      return 'C'
    else:
      return 'F'

  # class method
  def getcount():
    return Student.count

  def get_name_marks(self):
    return (self.name, self.marks)