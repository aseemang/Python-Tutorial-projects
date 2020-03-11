

'''employee_file = open("exployees.txt", "a")'''
#\n gives new line these characters are called escape characters
'''employee_file.write("\nKelly - Customer Service")'''

'''employee_file.write("Toby - Human Resources")'''
#say we want to add another employee, can append to file
#use a w to override entire file and write new thing
employee_file = open("employees1.txt", "w")
employee_file.write("\nKelly - Customer Service")

employee_file.close()
#can use other stuff like webpages
employee_file = open("index.html", "w")

employee_file.write("<p>This is HTML</p>;")
employee_file.close()

