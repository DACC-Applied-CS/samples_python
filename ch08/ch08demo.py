print('\033c\n')
valid = False

while not valid:
	try:
		third_number = int(input('Enter a number between 1 and 10: '))
		while third_number < 1 or third_number > 10:
			print('Number should be between 1 and 10, please re-enter')
			third_number = int(input('Enter a number between 1 and 10: '))
		print('Your number is', third_number)
		valid = True
	except ValueError:
		print('Value must be numeric')


