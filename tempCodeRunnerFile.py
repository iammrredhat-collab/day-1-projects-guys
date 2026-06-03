import random

print("Welcome to the Stone, paper , sissors game")
options = ["stone","paper","sissors"]

opponent_choice = random.choice(options)
mahoraga = input(" what do you want to choose? stone, papper or sissors: ")

if mahoraga == opponent_choice:
    print("mahoraga nice you adapted to your opponent choice, tie!")

elif mahoraga == "stone" and opponent_choice == "sissors":
    print("Mahoraga wins! demolishing the opponent")

elif mahoraga == "paper" and opponent_choice == "stone":
    print("Nice adaption, mahoraga wins again!")

elif mahoraga == "sissors" and opponent_choice == "paper":
    print("adapted to winning? ")

else:
    print("Need to adapt more... you lose")    