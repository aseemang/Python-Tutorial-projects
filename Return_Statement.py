#sometimes we want info back from a function, that's what the return keyword lets us do
def cube(num):
    num*num*num


cube(3)
#nothing happened in the above
print(cube(3))
#says "none," instead:
def cube(num):
    return num*num*num

result = cube(4)
print(result)
#can't put anything after the return statement, it breaks you out of the function

