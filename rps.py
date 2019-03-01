import random


def take_input():
    while True:
        choice = input(
            "Choose either Rock(r) or Paper(p) or Scissors(s)").lower()
        if not (choice == "p" or choice == "r" or choice == "s"):
            print("Please enter valid Input")
        else:
            break
    return choice


def play_again():
    while True:
        conf = input("Do yo like to play more?(y/n)")
        if conf == "y" or conf == "n":
            if conf == "y":
                play_game()
            else:
                print("Bye Bye")
                break
        else:
            print("enter A valid Input")


def play_game():
    user = take_input()
    computer = ""
    rand = random.randrange(1, 4)
    if rand == 1:
        computer = "s"
    elif rand == 2:
        computer = "r"
    else:
        computer = "p"
    print("User shows", user)
    print("Computer shows", computer)
    # validate winner
    if computer == user:
        print("Ooops. Draw \n Keep trying...")
        play_game()
    else:
        # big if condition
        if (computer == "s" and user == "p") or (computer == "r" and user == "s") or (computer == "p" and user == "r"):
            print("Computer Wins")
            play_again()
        else:
            print("User Wins")


print("Welcome to Rock, Paper and Scissors Game")
play_game()
