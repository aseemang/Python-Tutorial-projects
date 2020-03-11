#want to create a "student" class
class Student:
    #want to create something called an initialized function
    #can use it to map out what attributes student should have
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        #the name of the student object is going to be equal to the name that we passed in, that's what "self" does.