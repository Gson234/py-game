import random
while True:
    choices =["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player= input("rock, paper, scissors :").lower()

    if computer == player:
        print(computer)
        print(player)
        print("Its a tie")
    elif player == "rock":
        if computer == "scissors":
            print(computer)
            print(player)
            print("You won")
        if computer == "paper":
            print(computer)
            print(player)
            print("You lose")
    elif player == "paper":
        if computer == "scissors":
            print(computer)
            print(player)
            print("You lose")
        if computer == "rock":
            print(computer)
            print(player)
            print("You win")
    elif player == "scissors":
        if computer == "paper":
            print(computer)
            print(player)
            print("You won")
        if computer == "rock":
            print(computer)
            print(player)
            print("You lose")
    play = input("wana play again (yes/no):  ")
    if play != "yes":
        break
print("game ended")