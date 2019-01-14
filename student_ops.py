def get_details(name, gender, roll, marks):
  return 'Name : ' + name + '\nGender : ' + gender + '\nRoll : ' + str(roll) \
    + '\nMarks : ' + str(marks)

def get_grade(marks):
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