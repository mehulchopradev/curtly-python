from xyz.supercoders.college.professor import Professor
from xyz.supercoders.college.student import Student
from photosession import PhotoSession

p1 = Professor(name='mehul', subjects=['Physics','Chemistry'], gender='m')
# print(p1.name)
# print(p1.subjects)

# print(p1.getdetails())

s1 = Student(name='curtly', gender='m', roll=10, marks=90)
# print(s1.getdetails())

print(p1) # mehul
# print(p1.__str__(p1))
print(s1) # curtly

name = 'mehul'
print(name) # mehul
# print(name.__str__(name))

PhotoSession.takephoto(s1)
PhotoSession.takephoto(p1)
PhotoSession.takephoto(32)
