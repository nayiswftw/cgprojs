def determine_winner(player1_roll, player2_roll, player1_name, player2_name):
    if player1_roll > player2_roll:
        print(player1_name + " wins this round!")
        return "player1"
    elif player2_roll > player1_roll:
        print(player2_name + " wins this round!")
        return "player2"
    else:
        print("It's a tie!")
        return "tie"
