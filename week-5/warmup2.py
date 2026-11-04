# warmup2 - entering a positive integer
guess = 0
while guess < 1:
    guess = (input("Enter a positive integer."))
    try:
        guess = int(guess)
    except:
        print("That is not a positive integer. Please try again.")
        guess = 0
    else:
        if guess <= 0:
            print("That is not a positive integer. Please try again.")
    
    
print(f"You got it! You entered: {guess}")   