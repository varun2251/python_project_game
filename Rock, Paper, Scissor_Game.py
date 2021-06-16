# import random module
import random

# Print multiline instruction
print("Welcome to Rock, Paper & Scissor Game!")
print("Rules in order to win this game are as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

while True:
    print("Enter choice: \n 1. Rock \n 2. Paper \n 3. Scissor \n")

    # take the input from user
    choice = int(input("User turn: "))

    # OR is the short-circuit operator
    # if any one of the condition is true
    # then it returns True Value

    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("Please Enter a valid input: "))

    # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    # print user choice
    print("User Choice is: " + choice_name)
    print("\nNow its Computer turn to choose....")

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of module random to select any random number between 1 to 3.
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value(by user)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    # condition for winning
    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("paper wins => ", end="")
        result = "Paper"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end="")
        result = "Rock"
    else:
        print("scissor wins =>", end="")
        result = "Scissor"

    # Printing either user or computer wins the game!
    if result == choice_name:
        print("<== Congrats! User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input()

    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break

# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")