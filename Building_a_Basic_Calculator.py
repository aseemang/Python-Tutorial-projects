
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)

#so if you run the above, it is wrong. By default python converts user input to string

#must convert user input (strings) into numbers

#use int function to convert into numbers
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)

print(result)

#problem with int function is that it only looks for whole numbers. Decimal input will break program.
#float function solves this
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)
#sometimes you only want user to enter integer but in case of calculator you want everything