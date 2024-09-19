# make it as complex as you want 
# i have made it small an simple 

name = input("What is your name? ")
print("Welcome", name, "to the adventure game!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come across a river, you can walk around it or swim across. Type walk to walk around and swim to swim across. ").lower()
    if answer == "walk":
        print("You walked around and reached the other side of the river.")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator.")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You come across a locked door. You can either pick the lock or find the key. Type pick to pick the lock or key to find the key. ").lower()
    if answer == "pick":
        print("You tried to pick the lock and broke it, now you are forever locked.")
    elif answer == "key":
        print("You found the key and went through the door.")
    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")

print("Thank you for trying", name)