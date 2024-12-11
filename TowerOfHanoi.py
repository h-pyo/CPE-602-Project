# "I pledge my honor that I have abided by the Stevens Honor System. - Harris Pyo"
# Professor Yett
# CPE 602 
# 12/8/2024

#Importing math class to use in the FrameStewart function when calculating the value for k (split)
import math

#Function for Tower of Hanoi puzzle that takes in the number of disks, a split location, the 3 rods, and the move list to append to
#Modularized function so that it can be utilized in the FrameStewart function
def TowerOfHanoi(numDisks, k, startRod, middleRod, endRod, moves):
  #Base case
  if (numDisks == 0):
    return
  
  #Recursively call to move the top n-1 disks from the start rod to the middle
  TowerOfHanoi(numDisks - 1, k, startRod, endRod, middleRod, moves)

  currentMove = "Disk " + str(numDisks + k) + " moves from " + str(startRod) + " to " + str(endRod)
  #Add the move to he move list to keep track
  moves.append(currentMove)
  #Printing disk movement
  print(currentMove)

  #Recursively call again to move the stack of disks from the middle to the end rod where the biggest disk was
  TowerOfHanoi(numDisks - 1, k, middleRod, startRod, endRod, moves)
  #Return the moves list
  return moves

#Function for the Frame-Stewart algorithm to solve Reve's puzzle that takes in the number of disks, the 4 rods, and the move list to append to
def FrameStewart(numDisks, startRod, midRod1, midRod2, endRod, moves):
  #Base case
  if (numDisks == 0):
    return
  
  #Calculating the value for k or split location in the stack using the equation found
  k = int((numDisks + 1) - round(math.sqrt((2 * numDisks) + 1)))

  #Printing the disk movement similar to how it was printed in the TowerOfHanoi function when k = 0
  if (k == 0):
    currentMove = "Disk " + str(numDisks + k) + " moves from " + str(startRod) + " to " + str(endRod)
    moves.append(currentMove)
    print(currentMove)
    return
  
  #Recursive calls to move the top split of the disks to one of the middle rods, then move the bottom half to the end rod, and moving the top stack to the end afterwards
  #Utilizing the TowerOfHanoi function since each stack in the split is essentially treated as its own Tower of Hanoi. Also, modularizes the the code more
  FrameStewart(k, startRod, endRod, midRod2, midRod1, moves)
  TowerOfHanoi(numDisks - k, k, startRod, midRod2, endRod, moves)
  FrameStewart(k, midRod1, startRod, midRod2, endRod, moves)


def main():
  #Prompting the user for their input on what they'd like to simulate
  print("Welcome to the Tower of Hanoi, please enter the details for this game")
  numDisks = int(input("Enter the number of disks: "))
  numRods = int(input("Classic Tower of Hanoi(3) or Reve's Puzzle(4) - Enter 3 or 4: "))

  #Input validation for the number of disks and to get rid of trivial cases for inputs
  while (numDisks < 1):
    numDisks = int(input("Please enter a number greater than 0: "))
  while (numRods != 3 and numRods != 4):
    numRods = int(input("Please enter 3 or 4: "))
  
  #Moves list to keep track of the moves made if needed to debug and to also use when getting the total number of moves
  moves = []
  #Rods list that is generated based on if the user enters 3 or 4, which will create an array of numbers to represent the rods, which can be expanded to any number of rods
  rods = []
  for (i) in range(numRods):
    rods.append(i)

  #Run the Tower of Hanoi simulation or Reve's Puzzle depending on if the user enters 3 or 4 pegs for their input
  if (numRods == 3):
    TowerOfHanoi(numDisks, 0, rods[0], rods[1], rods[2], moves)
  elif (numRods == 4):
    FrameStewart(numDisks, rods[0], rods[1], rods[2], rods[3], moves)

  #Output the result of the game's simulation back to the user
  print(f"This setup for Tower of Hanoi/Reve's puzzle with {numDisks} disks and {numRods} rods takes {len(moves)} moves!")


#1 - Given a positive integer n for Tower of Hanoi
#2 - Given a positive integer n for Reve's Puzzle/Frame-Stewart algorithm
#6 - Verify Reve's Program
main()

#4 - All the moves to solve Tower of Hanoi puzzle with 10 Disks
# moves = []
# TowerOfHanoi(10, 0, "A", "B", "C" , moves)
# print(f"This setup for Tower of Hanoi with 10 disks takes {len(moves)} moves!")

#5 - All the moves to solve Reve's Puzzle with 20 Disks
# moves = []
# FrameStewart(20, "A", "B", "C", "D", moves)
# print(f"This setup for Reve's puzzle with 20 disks takes {len(moves)} moves!")