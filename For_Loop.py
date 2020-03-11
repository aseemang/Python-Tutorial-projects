
#for every letter in giraffe academy, I want to do something
for letter in "Giraffe Academy":
    print(letter)
#the variable will change in each iteration of the loop
#can also use for arrays
friends = ["Jim", "Karen", "Kevin"]
#for each friend in the friends array, I want to print out the friend
#the "friend" after the for could be anything (could be "name")
for friend in friends:
    print(friend)
for name in friends:
    print(name)
#can also loop through series of numbers
for index in range(10):
    print(index)
for index in range(3, 10):
    print(index)
#could use a range to loop through an array
for index in range(len(friends)):
    print (friends[index])
#can use all sorts of logic inside the for loops
for index in range(5):
    if index == (0):
        print("first iteration")
    else:
        print("not first")
