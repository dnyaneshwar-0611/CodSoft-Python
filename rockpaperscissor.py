#Rock-Paper-Scissor Game

import random

choices =["rock","paper","scissor"]

while True:

    user_choice =input("Enter Your choice from below Options:\n1.rock \n2.paper \n3.scissor\n")
    computer_choice= random.choice(choices)

    print("User Choice:", user_choice)
    print("Computer Choice: ",computer_choice)

    if user_choice==computer_choice:
        print("Tie !!")

    elif user_choice=="rock" and computer_choice=="scissor":
        print("You win !!")

    elif user_choice=="paper" and computer_choice=="rock":
        print("You win !!")

    elif user_choice=="scissor" and computer_choice=="paper":
        print("You win !!")

    else:
        print("You lose !!")

    print("You want to play again? (y/n)")
    ans= input().lower
    
    if ans=='n':
        break

print("Thanks for playing this game !!!")