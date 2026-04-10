def show_winner(player1_name, player2_name, player1_wins, player2_wins):
    print()
    print("=" * 40)
    print("GAME OVER")
    print("=" * 40)
    print()
    if player1_wins > player2_wins:
        print(player1_name + " wins the game!")
    else:
        print(player2_name + " wins the game!")
    print()
