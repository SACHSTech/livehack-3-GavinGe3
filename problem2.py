"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  Allows user to input the distance in km they driven each day until the total distance surpasses 100, the program then outputs the number of days it took to surpass 100km driven and the average distance driven per day
 
Author: Ge.G
 
Created:  03/03/2021
------------------------------------------------------------------------------
"""
print("***** Welcome to the DoorDash Distance Tracker *****")

# initiates variable for the number of days and total distance driven
days = 0
totalDistance = 0

print("\n** Travel Log **")

# allows user to input distance driven each day until total distance surpasses 100km, adds each distance and 1 to the total distance and days variables
while totalDistance <= 100:
  totalDistance += float(input("Enter the distance travelled for the day: "))
  days += 1

# outputs the number of days it took to surpass 100km and the average km travelled per day
print("\n ** Summary **")
print(f"It took {days} days to surpass 100km driven.")
print(f"The average distance driven per day is {round(totalDistance / days)} km.")