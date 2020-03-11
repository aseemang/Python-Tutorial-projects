is_male = True
is_tall = True

#if is_male or is_tall:
    #print("You are a male or tall or both")
    #else means otherwise
#else:
    #print("You are either not male or not tall both")
#can use and to require both variables to be true
if is_male and is_tall:
    print("You are a tall male")
#else:
   # print("You are either not male or not tall both")
#can use elif to put another condition and 'not' to negate whatever is in parenthesis
elif is_male and not(is_tall):\
    print("You are a short male")
elif not(is_male) and is_tall:\
    print("You are a not a male but are tall")
else:
    print("Youa re not a male and not tall")


