number = 10

print("I'm thinking of a number...")
while True:
    guess = (input("What number am I thinking of? "))
    if guess == "q":
        print(f"Sorry! The number was {number}.")
        break
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Sorry! Try Again.")
        if int(guess)>number:
            print("Your guess was too high")
        else:
            print("Your guess was to low")
