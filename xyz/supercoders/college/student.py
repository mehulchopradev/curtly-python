from xyz.supercoders.college.collegeuser import CollegeUser # parent class (super class)
# Student -> CollegeUser -> object
class Student(CollegeUser): # child class (sub class)

  # class attributes
  count = 0

  def __init__(self, name, roll, gender, marks, mobilenos=[]):
    # constructor
    # configuring/adding attributes to the object
    super().__init__(name, gender, mobilenos)
    # CollegeUser.__init__(self, name, gender, mobilenos)

    self.roll = roll
    self.marks = marks

    Student.count += 1

  @property
  def roll(self):
    return self.__roll

  @roll.setter
  def roll(self, roll):
    if roll > 0:
      self.__roll = roll
    else:
      self.__roll = None

  # method overriding
  def getdetails(self):
    str1 = super().getdetails()

    str2 = 'Roll: {0}\nMarks : {1}'.format(self.roll, self.marks)

    return str1 + str2

  # object methods
  '''def getdetails(self):
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
    
    return str1 + str2'''

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