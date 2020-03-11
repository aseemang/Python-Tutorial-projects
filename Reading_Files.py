
#use open to open file. exployees.txt in same directory so can just say file name
#must specify which mode you want to open file in.
#"r" means read
#"w" means write
#"a" means append
#"r+" means read and write
#we generally want to store this in a variable, so:
employee_file = open("exployees.txt", "r")
#it's a good idea to make sure that's it's possible to read the file

print(employee_file.readable())
#print(employee_file.read())
#can also read individual lines from file
'''print(employee_file.readline())'''
#when you say it again, it reads the line after that
'''print(employee_file.readline()'''
#can use readlines to print all lines in a file as a list
for employee in employee_file.readlines():
    print(employee)

'''print(employee_file.readlines()[1])'''
#always make sure we close the file as well
employee_file.close()

