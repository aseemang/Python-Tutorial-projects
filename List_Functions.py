
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
#extend function lets you add another list onto a list
#friends.extend(lucky_numbers)
print(friends)
#append lets you append another item onto end of list
friends.append("Creed")
print(friends)
#insert lets you add into middle of list when given parameters
friends.insert(1, "Kelly")
print(friends)
#can use remove to remove values from list
friends.remove("Jim")
print(friends)
#can use clear to get rid of everything
#friends.clear()
print(friends)
#pop lets you remove last element from list
friends.pop()
print(friends)
#can use index to check if certain value is in list
print(friends.index("Kevin"))
#print(friends.index("Mike"))
#can use count to see how many times something appears in list
print(friends.count("Jim"))
#can use sort to put in alphabetical order or numerical or
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
#can use reverse function to reverse list order
lucky_numbers.reverse()
print(lucky_numbers)

#use copy to copy a list
friends2 = friends.copy()
print(friends2)