import os
def main():
	os.system('clear')
	print('''PASSWORD VERIFIER:\n==================== \nPasswords must:
	- be 6 or more characters
	- have at least one lower case letter
	- have at least one upper case letter
	- have at least one digit	''')
	while True:
		password = input("\nEnter your password: ")
		if is_valid(password):
			break
		else:
			continue

def has_upper(string):
	for ch in string:
		if ch.isupper():
			return True
	return False

def has_lower(string):
		for ch in string:
			if ch.islower():
				return True
		return False

def has_digit(string):
		for ch in string:
			if ch.isdigit():
				return True
		return False

def has_length(string):
	return len(string) > 5

def is_valid(string):
	upper = has_upper(string)
	lower = has_lower(string)
	digit = has_digit(string)
	length = has_length(string)
	if upper and lower and digit and length:
		print("Password is valid")
		return True
	else:
		print("\nPassword is invalid for the following reasons:")
	if not upper:
		print("- Missing an uppercase letter")
	if not lower:
		print("- Missing a lowercase letter")
	if not digit:
		print("- Missing a digit")
	if not length:
		print("- Not long enough")
	return False

main()