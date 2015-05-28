# import numpy as np
import random
# import click

# Define state indices
rock = 0
paper = 1
scissors = 2
total = 3

# Define the array, empty: [[0,0,0],[0,0,0],[0,0,0]]
state = [[0 for x in range(3)] for x in range(3)]

# Get user input
def userMove():
	uM = raw_input('Enter R, S, or P:  ')
	if uM == 'R' or uM == 'r':
		uM = rock
	elif uM == 'S' or uM == 's':
		uM = scissors
	elif uM == 'P' or uM == 'p':
		uM = paper
	elif uM == 'state':
		print state
		uM = userMove()
	else:
		print "Try again."
		uM = userMove()
	return uM

def compMove(olduM):
	global state
	focus = state[olduM]
	# It needs to select what's gonna beat the probable move
	probList = [paper]*focus[rock] + [scissors]*focus[paper] + [rock]*focus[scissors]
	if len(probList) == 0:
		probList = [rock, paper, scissors]
	cM = random.choice(probList)
	return cM

def getWinner(uM, cM):
	winMap = [[0,-1,1],[1,0,-1],[-1,1,0]]
	return winMap[uM][cM]

def updateState(state, olduM, uM):
	state[olduM][uM] += 1
	return state

# Main loop
def main():
	# Initialize scoreboard
	userWins = 0
	compWins = 0
	# Initialize arbitrary last move
	olduM = 0

	isntFirstTurn = False

	while (True):
		global state
		global isntFirstTurn

		# Print scoreboard // last move -- just do the print in this line
		print "USER: " + str(userWins) + " // COMP: " + str(compWins)
		# Get user move
		uM = userMove()
		# Get computer response
		cM = compMove(olduM)
		# Get winner, update stats
		winner = getWinner(uM, cM)
		if winner == 1:
			userWins += 1
			print "YOU WIN!"
		elif winner == -1:
			compWins += 1
			print "YOU LOSE!"
		else:
			print "TIE!"
		if isntFirstTurn == True:
			state = updateState(state, olduM, uM)
		else:
			isntFirstTurn = True
			print "Was first turn!"
		olduM = uM

main()