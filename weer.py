import random
import time
number = random.randint(1, 100)
def intro():
    name = input("What is your name? ")
    print(name, "ok now you will have to guess a number from 1 to 100.")
    print("I will give you hints. You have 5 chances.\n")
    if number % 2 == 0:
        print("First hint: The number is even.")
    else:
        print("First hint: The number is odd.")
    time.sleep(0.5)
    print("Now guess!\n")
def pick():
    guesses_taken = 0
    while guesses_taken < 5:
        try:
            guess = int(input("Guess: "))
            if guess < 1 or guess > 100:
                print("That's not in range. Please enter a number between 1 and 100.\n")
                continue
            guesses_taken += 1
            if guess < number:
                print("Too low!\n")
            elif guess > number:
                print("Too high!\n")
            else:
                print("🎉 Correct! You guessed the number!")
                return
        except:
            print("I don't think that is a number.\n")
    print("Sorry, you ran out of guesses.")
    print("The number was:", number)
intro()
pick()