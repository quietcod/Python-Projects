import random
user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']
while True:
    user_input = input("Type Rock, Paper or Scissors (or 'q' to quit): ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Invalid input, please try again.")
        continue

    random_number = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2 = scissors
    compuer_pick = options[random_number]
    print("Computer picked", compuer_pick + ".")

    if user_input == 'rock' and compuer_pick == 'scissors':
        print("You win!")
        user_wins += 1
        continue
    elif user_input == 'paper' and compuer_pick == 'rock':
        print("You win!")
        user_wins += 1
        continue
    elif user_input == 'scissors' and compuer_pick == 'paper':
        print("You win!")
        user_wins += 1
        continue
    else:
        print("You lose!")
        computer_wins += 1
    
print("You have won", user_wins, "times.")
print("The computer has won", computer_wins, "times.")
print("Goodbye!")