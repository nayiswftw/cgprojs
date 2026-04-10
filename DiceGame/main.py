from roll import roll_dice
from winner import determine_winner
from score import show_score
from game_over import show_winner

print("Welcome to the Dice Rolling Game!")
print()

player1_name = input("Enter first player name: ")
player2_name = input("Enter second player name: ")
print()

player1_wins = 0
player2_wins = 0
round_number = 1
game_history = []

while player1_wins < 3 and player2_wins < 3:
    print("=" * 40)
    print("ROUND " + str(round_number))
    print("=" * 40)
    
    player1_roll = roll_dice()
    player2_roll = roll_dice()
    
    print(player1_name + " rolled: " + str(player1_roll))
    print(player2_name + " rolled: " + str(player2_roll))
    print()
    
    winner = determine_winner(player1_roll, player2_roll, player1_name, player2_name)
    
    game_history.append([round_number, player1_name, player1_roll, player2_name, player2_roll, winner])
    
    if winner == "player1":
        player1_wins = player1_wins + 1
    elif winner == "player2":
        player2_wins = player2_wins + 1
    
    print()
    show_score(player1_name, player2_name, player1_wins, player2_wins)
    
    round_number = round_number + 1
    
    if player1_wins < 3 and player2_wins < 3:
        input("Press Enter to continue to the next round...")
        print()

show_winner(player1_name, player2_name, player1_wins, player2_wins)
