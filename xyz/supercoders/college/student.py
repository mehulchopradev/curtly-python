class Student:

  def __init__(self, name, roll, gender, marks):
    # constructor
    # configuring/adding attributes to the object
    self.name = name
    self.roll = roll
    self.gender = gender
    self.marks = marks

  def getdetails(self):
    return 'Name : ' + self.name + '\nGender : ' + self.gender + '\nRoll : ' + str(self.roll) \
    + '\nMarks : ' + str(self.marks)

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