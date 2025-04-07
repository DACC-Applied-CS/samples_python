##===================================================
# ## The following clears the screen before code runs
print('\033c\n')
##===================================================

# simple while loop
print("\nPrint using a while loop:")
number = 0

while number < 11:
	print(number, end=" ")
	number += 1
print("\n")

# ###############################################
print("\nUsing a while loop for input validation:")
while True:
	number2 = int(input("Enter a number between 1 and 10: "))
	if number2 < 1 or number2 > 10:
		print("Invalid")
		continue
	else:
		print("Valid number:", number2)
		break
print("\n")

###############################################
print("\nAnother way to do the same input validation:")
number2 = int(input("Enter a number between 1 and 10: "))
while number2 < 1 or number2 > 10:
	print("Invalid")
	number2 = int(input("Enter a number between 1 and 10: "))

###############################################
print("\nCounting down with a while loop:")
number4 = 10

while number4 > 0:
    print(number4, end=" ")
    number4 -= 1
    
print()
print()