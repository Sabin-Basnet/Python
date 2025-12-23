import random

num=random.randint(1,100)
guess = 0

while (True):
    user_guess = int(input("Enter your guess between(1-100):    "))

    if(user_guess == num):
        guess+=1
        print(f"You gueeses the number {num} correct in {guess} attempt")
        break

    elif(user_guess < num):
        guess+=1
        print("You gussed it lower ")

    else:
        guess+=1
        print("You guessed it higher")

