from xyz.supercoders.college.collegeuser import CollegeUser

class PhotoSession:

  def takephoto(person):
    if isinstance(person, CollegeUser):
      print('Photo taken of {0}'.format(person.name))
    else:
      print('hey pass in the right guys')