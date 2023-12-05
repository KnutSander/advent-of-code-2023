#!/usr/bin/env python3

"""
" part2.py
"
" Your calculation isn't quite right. It looks like some of the digits are 
" actually spelled out with letters: one, two, three, four, five, six, seven, 
" eight, and nine also count as valid "digits".
"
" Equipped with this new information, you now need to find the real first and 
" last digit on each line. For example:
"
" two1nine
" eightwothree
" abcone2threexyz
" xtwone3four
" 4nineeightseven2
" zoneight234
" 7pqrstsixteen
"
" In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
" Adding these together produces 281.
"""

#-------------------------------------------------------------------------------
# Imports and Global Variables
#-------------------------------------------------------------------------------

import re

# Initialise string to number convertion
digit_values = {'one': '1', 
					'two': '2', 
					'three': '3', 
					'four': '4', 
					'five': '5',
                    'six': '6', 
                    'seven': '7', 
                    'eight': '8', 
                    'nine': '9'}

# Intialise the total variable
total = 0

#-------------------------------------------------------------------------------
# Routines
#-------------------------------------------------------------------------------

def extract_numeric_values(parts):
	numeric_values = []

	for part in parts:
		# Check if the part is a numeric value
		if part.isdigit():
			numeric_values.append(part)
		else:
			# Find matches of spelled-out digits
			matches = re.findall(r'(one|two|three|four|five|six|seven|eight|nine)', part.lower())

			# Convert spelled-out digits to numeric equivalents
			for match in matches:
				numeric_values.append(digit_values[match])

	return numeric_values

#-------------------------------------------------------------------------------
# Main Program
#-------------------------------------------------------------------------------

# Read each line of the input file
with open('input', 'r') as file:
	for line in file:
		# Split line based on numeric characters
		line_parts = re.split(r'(\d)', line)

		# Extract numeric values into list
		numeric_values = extract_numeric_values(line_parts)

		# Concatenate the first and last numbers
		whole_number = int(numeric_values[0] + numeric_values[-1])
		print(whole_number)

		# Add the number to the total
		total += whole_number


# Print the total
print("Total sum:", total)