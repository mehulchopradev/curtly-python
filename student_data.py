from student_ops import get_details, get_grade

# Student
name = input('Enter name : ')
roll = int(input('Enter roll : '))
gender = input('Enter gender : ')
marks = float(input('Enter marks : '))

print(get_details(name, gender, roll, marks))
print(get_grade(marks))

# procedural way of programming

# object oriented programming (Real World -> Software world)
# Representing real world actors in software (Real world student should be allocated some memory in the RAM)
  # for a actor in real world -> object in software world (Object -> occupies memory in the RAM)
  # object has a data type -> Student (class)
# Characteristics of real world actors -> Attributes of that object in the RAM
  # All objects corresponding to the actors must have same uniform set of attributes
# Actions on real world actprs -> Methods called on those objects