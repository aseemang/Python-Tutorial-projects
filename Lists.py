#define lists much like variables, but use square brackets to input info
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# can put strings, numbers, booleans in lists, python is fine with it

print(friends)
#print out specific elements in lists by referring to their index, which starts at 0
print(friends[0])
#can also access elements based on their position from back of list, which start at -1
print(friends[-1])
#can define which section of elements to grab, does NOT grab last number in range
print(friends[1:3])
#can modify elements in list
friends[1] = "Mike"
print(friends[1])
