from xyz.supercoders.college.collegeuser import CollegeUser
# Professor -> CollegeUser -> object (Multi level inheritance)
class Professor(CollegeUser):

  def __init__(self, name, gender, subjects, mobilenos=[]):
    super().__init__(name, gender, mobilenos)

    self.subjects = subjects

  # overrides (method overriding)
  # proper override is the signature of the functions should be the same
  def getdetails(self):
    str1 = super().getdetails()
    # CollegeUser.getdetails(self)

    str2 = ''
    if self.subjects:
      str2 = ','.join(self.subjects)
    else:
      str2 += 'No subjects taught'

    return str1 + str2