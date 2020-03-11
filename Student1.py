class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
#we can use functions inside class files
#say we want to create funtion that told us if student was on honor role
    def on_honor_role(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False