#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Imports and Global Variables
#-------------------------------------------------------------------------------

# Initialise the colour amounts
red = 12
green = 13
blue = 14 

# Initialise possible game variable
game_values = 0

#-------------------------------------------------------------------------------
# Routines
#-------------------------------------------------------------------------------

def is_count_possible(count, colour):
	return count <= globals()[f'{colour}']

#-------------------------------------------------------------------------------
# Main Program
#-------------------------------------------------------------------------------

# Read each line of the input file
with open('input', 'r') as file:
	for game_number, line in enumerate(file, start=1):

		# Initialise each game as possible
		game_possible = True

		# Split between game and game sets of balls
		game, game_sets = line.strip().split(':')
		
		# Seperate each game set into a separate string
		game_sets = game_sets.strip().split(';')

		# Check if each game set is possible
		for game_set in game_sets:

			# Split each game set into independant moves
			moves = game_set.strip().split(',')

			# Check if each move is possible
			for move in moves:
				count, colour = move.strip().split()
				count = int(count)

				# Check if move is possible using lambda function
				if not is_count_possible(count, colour):
					game_possible = False
					break

		# Check if the game is possible and add it to the total value
		if game_possible:
			game_values += game_number


print(game_values)