from datetime import date

def invalid_date(date_string):
	return "%s is illegal" % date_string

def convert_int_to_year(unformatted_int):
		f = str(unformatted_int)
		if len(f) == 1:
			return int('200'+f)
		elif len(f) == 2:
			return int('20'+f)
		return int(f)

def check_date(date_string):

	import itertools
	# new approach, try and force all possible answers and pick the lowest date if one exists
	possible_answers = []

	date_string = date_string.split('/')
	if not len(date_string) == 3:
		invalid_date(date_string)
		return
	
	date_numbers = [int(date_string[0]),int(date_string[1]),int(date_string[2])]
	for i in itertools.permutations(date_numbers):
		try:
			possible_answers.append(date(i[0],i[1],i[2]))
		except ValueError:
			pass
	
	if not any([True for d in date_numbers if d > 1000]):
		date_set_1 = [convert_int_to_year(date_numbers[0]),date_numbers[1],date_numbers[2]]
		date_set_2 = [date_numbers[0],convert_int_to_year(date_numbers[1]),date_numbers[2]]
		date_set_3 = [date_numbers[0],date_numbers[1],convert_int_to_year(date_numbers[2])]

		for i in itertools.permutations([date_set_1[1],date_set_1[2]]):
			try:
				possible_answers.append(date(date_set_1[0],i[0],i[1]))
			except ValueError:
				pass

		for i in itertools.permutations([date_set_2[0],date_set_1[2]]):
			try:
				possible_answers.append(date(date_set_2[1],i[0],i[1]))
			except ValueError:
				pass

		for i in itertools.permutations([date_set_3[0],date_set_1[1]]):
			try:
				possible_answers.append(date(date_set_3[2],i[0],i[1]))
			except ValueError:
				pass

	final_answers = []
	if possible_answers:
		EARLIEST = date(2000,1,1)
		LATEST = date(2999,12,31)

		for a in possible_answers:
			if a < EARLIEST or a > LATEST:
				continue
			final_answers.append(a)
		
	final_answers.sort()

	if not final_answers:
		return invalid_date(date_string)

	return final_answers[0]

def main(argv=None):
	# For now we are assuming the input is coming from the command line
	# although the puzzle mentions a file so we might have to take that into account instead
	date_string = argv or ' '.join(sys.argv[1:])

	print check_date(date_string)

if __name__ == "__main__":
	sys.exit(main())


