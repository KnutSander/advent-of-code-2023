#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Main Program
#-------------------------------------------------------------------------------

# Intialise the total variable
total = 0

# Read each line of the input file
with open('input', 'r') as file:
	for line in file:
		# Extract the numbers from the line
		numbers = [char for char in line if char.isdigit()]

		# Skip the line if it contains no numbers
		if not numbers:
			continue

		# Concatenate the first and last numbers
		whole_number = int(numbers[0] + numbers[-1])

		# Add the number to the total
		total += whole_number

# Print the total
print("Total sum:", total)