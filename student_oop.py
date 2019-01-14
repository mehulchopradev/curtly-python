from xyz.supercoders.college.student import Student

s1 = Student('mehul', 32, 'm', 90)
'''
1. Memory will be reserved in the RAM - 4001
2. Student.__init__(4001, 'mehul', 32, 'm', 90)
'''


s2 = Student('jane', 30, 'f', 40)
'''
1. Memory will be reserved in the RAM - 4003
2. Student.__init__(4003)
'''

#print(id(s1))
#print(id(s2))

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
s3 = Student('jill', 10, 'f', 90)

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

print(s1.getgrade())
print(s2.getgrade())

