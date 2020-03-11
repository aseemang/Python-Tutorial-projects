
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
#must use while loop to continuously ask person to guess word until they get it right

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
  #two possibile ways loop can end: either guess correctly or out of guesses, so:
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You Win!")
#can make a better game than this though, let's set limit
