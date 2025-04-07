import os

def main():
	os.system('clear')
	my_string = "abcdef123ABC"
	print("My string is: ",my_string)
	print("There are", count_lower(my_string),"lowercase letters")
	print("There are", count_upper(my_string),"uppercase letters")
	print("There are", count_digit(my_string),"digits")
	print("\n"*3)

def count_lower(str_var):
	lower = 0
	for ch in str_var:
		if ch.islower():
			lower += 1
	return lower

def count_upper(str_var):
	upper = 0
	for ch in str_var:
		if ch.isupper():
			upper += 1
	return upper

def count_digit(str_var):
	digit = 0
	for ch in str_var:
		if ch.isdigit():
			digit += 1
	return digit


# call the main() function:
main()