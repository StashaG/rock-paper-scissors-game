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
print()

if player_1_move == player_2_move:
  print("We have a tie! 🚀")
elif player_1_move == "R" and player_2_move == "S":
  print("Player 1 is the winner 🥳")
elif player_1_move == "S" and player_2_move == "P":
  print("Player 1 is the winner 🎊")
elif player_1_move == "P" and player_2_move == "R":
  print("Player 1 is the winner 💃🏽")
elif player_1_move == "S" and player_2_move == "R":
  print("Player 2 is the winner 🍾")
elif player_1_move == "P" and player_2_move == "S":
  print("Player 2 is the winner 🙌🏾")
elif player_1_move == "R" and player_2_move == "P":
  print("Player 2 is the winner 🎉")
else:
  print("This is not valid. Try again .")
