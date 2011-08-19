import sys
import re
from datetime import date

"""
We have four different regex here
3 account for a 4 digit year
The last one  has an ambiguous year
1.	\d{4}/\d{1,2}/\d{1,2}$
2.	\d{1,2}/\d{4}/\d{1,2}$
3.	\d{1,2}/\d{1,2}/\d{4}$
4.	\d{1,2}/\d{1,2}/\d{1,2}$
"""

valid_date = re.compile('(\d{4}/\d{1,2}/\d{1,2}$)|(\d{1,2}/\d{4}/\d{1,2}$)|(\d{1,2}/\d{1,2}/\d{4}$)|(\d{1,2}/\d{1,2}/\d{1,2}$)')

def invalid_date(date_string):
	print "%s is illegal" % date_string

def main(argv=None):
	# For now we are assuming the input is coming from the command line
	# although the puzzle mentions a file so we might have to take that into account instead
	date_string = argv or ' '.join(sys.argv[1:])

	# if it doesn't match our regex, it is invalid
	match = valid_date.match(date_string)
	if not match:
		return invalid_date(date_string)

	match_list = match.groups()

	# We aren't quite sure what the year/month/days are since we base it off the minimum date aka the lowest integers
	num_1 = 0
	num_2 = 0
	num_3 = 0
	year = 0

	# Go through each regex match (1,4) and setup the variables for consumption next
	if match_list[0]:
		year = date_string.split('/')[0]
		num_1 = date_string.split('/')[1]
		num_2 = date_string.split('/')[2]
	elif match_list[1]:
		year = date_string.split('/')[1]
		num_1 = date_string.split('/')[0]
		num_2 = date_string.split('/')[2]
	elif match_list[2]:
		year = date_string.split('/')[2]
		num_1 = date_string.split('/')[0]
		num_2 = date_string.split('/')[1]
	elif match_list[3]:
		num_1 = date_string.split('/')[0]
		num_2 = date_string.split('/')[1]
		num_3 = date_string.split('/')[2]

	# convert to integer for comparison below
	num_1 = int(num_1)
	num_2 = int(num_2)
	num_3 = int(num_3)
	year = int(year)

	# ordering is like so year,month,day from low->high
	day = num_1
	month = num_2
	if num_2 > num_1:
		day = num_2
		month = num_1

	# if our last regex is the winner, then we have to compare the year as well
	if num_3:
		year = num_3
		if num_3 > day:
			year = month
			month = day
			day = num_3
		elif num_3 > month:
			year = month
			month = num_3

	# our year could be a single digit or double digit, we need to convert it to 4 digits
	if len(str(year)) == 1:
		year = int('200'+str(year))
	elif len(str(year)) == 2:
		year = int('20'+str(year))

	# if our year,month,day values don't fit in the std library date function
	# then we know it's not a valid date
	try:	
		print date(year,month,day)
	except ValueError:
		invalid_date(date_string)

if __name__ == "__main__":
    sys.exit(main())

