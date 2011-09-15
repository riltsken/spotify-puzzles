import sys	
import itertools
from datetime import date

EARLIEST = date(2000,1,1)
LATEST = date(2999,12,31)

def invalid_date(date_string):
	return "%s is illegal" % date_string

# convert an integer to the year 2000
# ex 0 = 2000, 01 = 2001, 300 = 2300
def convert_year(year):
	converted_year = year + 2000
	if converted_year > 2999 or converted_year < 1:
		return year 
	return converted_year

# new approach, try and find all possible answers and pick the lowest date if one exists
def validate_date(date_string):
	date_string_split = date_string.split('/')
	more_than_four_or_quad_zero_or_tri_zero = \
		[True for s in date_string_split if (len(s) > 4 or s == '0000' or s == '000' or not s)]
	if not len(date_string_split) == 3 or more_than_four_or_quad_zero_or_tri_zero:
		return invalid_date(date_string)
	
	date_numbers = [int(date_string_split[0]),int(date_string_split[1]),int(date_string_split[2])]	
	
	# the year can be any of these three states
	# using permutations we dont really have to worry about order
	# sets = [
	#	[A,B,C]
	#	[convert(A),B,C]
	#	[convert(B),A,C]
	#	[convert(C),A,B]
	#	]
	date_sets = [
		[date_numbers[0],date_numbers[1],date_numbers[2]],
		[convert_year(date_numbers[0]),date_numbers[1],date_numbers[2]],
		[convert_year(date_numbers[1]),date_numbers[0],date_numbers[2]],
		[convert_year(date_numbers[2]),date_numbers[0],date_numbers[1]]
	]
	
	possible_answers = []
	for x, data in enumerate(date_sets):
		permutate_me = [data[1],data[2]] # year is handled separate
		if x == 0:
			permutate_me = [data[0],data[1],data[2]] # year is the same
		for i in itertools.permutations(permutate_me):
			try:
				if x == 0:
					test_date = date(i[0],i[1],i[2])
				else:	
					test_date = date(data[0],i[0],i[1])
			except ValueError:
				continue

			if test_date >= EARLIEST and test_date <= LATEST:
				possible_answers.append(test_date)

	if not possible_answers:
		return invalid_date(date_string)

	possible_answers.sort()
	return possible_answers[0]

def main(argv=None):
	# Assuming the input is coming from the command line 
	# but we can use it as a function as well
	date_string = argv or ' '.join(sys.argv[1:])

	print validate_date(date_string)

if __name__ == "__main__":
	sys.exit(main())

