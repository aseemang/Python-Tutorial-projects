'''using the student.py file
#we have created the template for what a student is, now we will create the student
#by giving info, we create the object
#student is the class, and actual student(data filled in) is the object'''
from student import Student
#first is refering to the file, second is referring to the class

#student 1 is a student object
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.gpa)
print(student2.is_on_probation)

#can model any real world entity with this