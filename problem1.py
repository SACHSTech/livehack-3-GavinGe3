"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Allows the user to input the results from 6 games in the tournament, and outputs which group they are placed in or if they are eliminated fromt the tournament
 
Author: Ge.G
 
Created:  03/03/2021
------------------------------------------------------------------------------
"""
print("***Welcome to the Tournament Tracker****")

# initiate a variable for counting wins 
wins = 0

# prompts the user for input that is taken in the upcoming for loop
print("\nEnter the wins and losses for your team (input W or L): ")

# Allows the user to input their results from 6 games
for i in range(6):
  winOrLose = input()
  if winOrLose == "W":
    wins += 1
  
# determines and outputs which group the team is placed in or if they have been elminated
if wins > 4:
  print("Your team is in Group 1")
elif wins > 2 and wins < 5:
  print("Your team is in Group 2")
elif wins > 0 and wins < 3:
  print("Your team is in Group 3")
else:
  print("Your team is eliminated from the tournament")