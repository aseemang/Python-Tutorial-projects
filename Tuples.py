#tuple is a container where you can store different values. Similar to lists but key differences
#tuple uses open and close parentheses, lists use square brackets
coordinates = (4, 5)
#tuple is immutable, means it can't be changed or modified
print(coordinates[1])
#coordinates[1] = 10 gets error because it's immutable
#people use tuples for data that is never gonna change

#can create a list of tuples but they still can't be changed
coordinates_tuples_list = [(4, 5), (6, 7), (80, 34)]
print(coordinates_tuples_list)







