from xyz.supercoders.college.student import Student

print(Student.getcount()) # 0
# class functions
# Student.getcount()

# list of str objects
s1 = Student('mehul', 32, 'm', 90, ['987689768','98657890768'])
name, marks = s1.get_name_marks()
print('Name : ' + name)
print('Marks : ' + str(marks))
'''
1. Memory will be reserved in the RAM - 4001
2. Student.__init__(4001, 'mehul', 32, 'm', 90)
'''


s2 = Student('jane', 30, 'f', 40, '09876547896')
'''
1. Memory will be reserved in the RAM - 4003
2. Student.__init__(4003)
'''

#print(id(s1))
#print(id(s2))

print(Student.getcount())

'''s1.name = 'mehul'
s1.roll = 32
s1.gender = 'm'
s1.marks = 90

s2.name = 'jane'
s2.roll = 30
s2.gender = 'f'
s2.marks = 40

print(s1.name)
print(s2.name)
print(s1.roll)
print(s2.roll)'''

# bad
s3 = Student('jill', 10, 'f', 69)

# free to assign any more attributes
s3.student_name = 'jill'
s3.r = 10
s3.gender = 'f'
s3.subjectmarks = 90

'''print(s3.name)
print(s1.roll)
print(s2.roll)'''

# print(s1.getdetails())
# Student.getdetails(s1)

# print(s3.getdetails())
# Student.getdetails(s3)

'''print(s1.getgrade())
print(s2.getgrade())

print(Student.getcount())'''

'''print(s1.getdetails())
print(s2.getdetails())
print(s3.getdetails())'''

# list of Student objects
slist = [s1, s2, s3]
smap = {32: s1, 30: s2, 10: s3}
'''for student in slist:
  print(student.getdetails())'''

# filtering
'''morethan40 = [student for student in slist if student.marks > 40]
for s in morethan40:
  print(s.getdetails())'''

roll = int(input('Enter roll : '))
'''for student in slist:
  if student.roll == roll:
    print(student.getdetails())
    break
else:
  # will execute if the corresponding for block is exhausted in its iteration of the sequence of elements
  print('Student not found')'''

if roll not in smap:
  print('Student not found')
else:
  student = smap[roll]
  print(student.getdetails())