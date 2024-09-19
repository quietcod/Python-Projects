import random
# r = random.randrange(-5, 11) # it will not include 11
# r = random.randint(0, 10) # it will include both 0 and 10
# print(r) # This will print a random number between 0 and 10

top_of_range = input("Type a Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_numer = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_numer:
        print("You got it!")
        break
    elif user_guess > random_numer:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses.")