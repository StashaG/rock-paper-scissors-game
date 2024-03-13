from getpass import getpass as input

print("EPIC Rock, Paper, Scissors GAME 🎲 🎮!")
print()
print(("Select your move (R, P, or S)"))
print()
player_1_move = input("Player 1: ")
print()
player_2_move = input("Player 2: ")
print()
print()
print("Player 1 entered: " + player_1_move)
print()
print("Player 2 entered: " + player_2_move)

if player_1_move == player_2_move:
  print("We have a tie!")
