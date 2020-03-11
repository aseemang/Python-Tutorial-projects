#this is 2^3
#print(2**3)
#we will create an exponent function that an do this with for loops
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 3))
#inside this function we're taking in two pieces of info, the base number and the power number
# defining a variable called result, where we will store the answer
#specified a for loop that wants to loop through the range of the pow nuwbers, all way the up to but not including  the pow
# number, basically looping through "power" number of times (if pow was included, that would be 4 times(python counts from 0)
#multiplying result times base num
#tldr, for every number in the specified range of pow num, we are multiplying THAT by the result, which equals result(1) times base
#so it for (2, 3) it would be 1*3, three times (1x3 * 1x3* 1x3*)