#function is a collection of code which performs specific task
#want to create a function that says hi to user

#def is a keyword which tells python you want to use a function
#all code after colon is inside function, but must indent
def say_hi():
    print("Hello User")

#now we must call the function
print("Top")
say_hi()
print("Bottom")
#usually want functions to be named in all lower case, longer names need underscores
#parameter is a piece of info that you give to the function
def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Mike", "35")
say_hi("Steve", "70")
#can past basically any type of data into a function



