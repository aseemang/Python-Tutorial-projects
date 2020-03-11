#can use a try except block to handle errors without whole program breaking


try:
    #still get invalid input bc of value, even though we didn't input anything
    #we can except specific types of erros
    value = 10 / 0
    number = int(input("Enter a number"))
    print(number)
#using just the except will catch any error ever
#can store except as a variable with "as"
#it is best practice to use specific errors
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

