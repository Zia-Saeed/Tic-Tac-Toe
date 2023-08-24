GB = ["___", "___", "___",
      "___", "___", "___",
      "___", "___", "___",
      ]

print("Welcome to Tic Tac Toe\n")


def game_board():
    print("A:  " + GB[0] + "│" + GB[1] + "│" + GB[2])
    print("B:  " + GB[3] + "│" + GB[4] + "│" + GB[5])
    print("C:  " + GB[6] + "│" + GB[7] + "│" + GB[8])
    print("       │   │ ")


def play_game():
    global GB
    positions = {
        "a1": 0, "a2": 1, "a3": 2, "b1": 3, "b2": 4, "b3": 5, "c1": 6, "c2": 7, "c3": 8,
    }

    while True:
        game_board()
        player1 = input('Enter your Position(like: a1 for first position) Player1: ')
        if player1 in positions:
            if GB[positions[player1]] == "___":
                GB[positions[player1]] = " X "
                break
            else:
                print("This place is already filled.")
        else:
            print("Invalid Input.")

    if win_check():
        GB = ["___", "___", "___",
              "___", "___", "___",
              "___", "___", "___",
              ]
        return True

    while True:
        game_board()
        player2 = input("Enter the Position Player2(like: b1 for fourth position): ")
        if player2 in positions:
            if GB[positions[player2]] == "___":
                GB[positions[player2]] = " O "
                break
            else:
                print("This place is already filled.")
        else:
            print("Invalid Input.")

    if win_check():
        GB = ["___", "___", "___",
              "___", "___", "___",
              "___", "___", "___",
              ]
        return True


def win_check():
    if GB[0] == GB[3] == GB[6] == " X " or GB[1] == GB[4] == GB[7] == " X " or GB[2] == GB[5] == GB[8] == " X ":
        print("Player1 Won!")
        return True
    elif GB[0] == GB[3] == GB[6] == " O " or GB[1] == GB[4] == GB[7] == " O " or GB[2] == GB[5] == GB[8] == " O ":
        print("Player2 Won!")
        return True
    elif GB[0] == GB[1] == GB[2] == " X " or GB[3] == GB[4] == GB[5] == " X " or GB[6] == GB[7] == GB[8] == " X ":
        print("Player1 Won!")
        return True
    elif GB[0] == GB[1] == GB[2] == " O " or GB[3] == GB[4] == GB[5] == " O " or GB[6] == GB[7] == GB[8] == " O ":
        print("Player2 Won!")
        return True
    elif GB[0] == GB[4] == GB[8] == " X " or GB[2] == GB[4] == GB[6] == " X ":
        print("Player1 Won!")
        return True
    elif GB[0] == GB[4] == GB[8] == " O " or GB[2] == GB[4] == GB[6] == " O ":
        print("Player2 Won!")
        return True
    if "___" not in GB:
        print("Draw match!")
        return True


def run_game():
    while True:
        if play_game():
            break
        play_game()


if __name__ == '__main__':
    run_game()

    while True:
        play_again = input("Do You Want To Play Again? y/n: ").lower().strip()
        if play_again == "no" or play_again == "n":
            break
        else:
            run_game()
