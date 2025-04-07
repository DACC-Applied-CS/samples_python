# ##===================================================
# ## The following clears the screen before code runs
print('\033c\n')
# ##===================================================

# for loop with simple range()
print("\nUsing a for loop with range:")
for nbr in range(1, 11):
	print(nbr, end=" ")
print("\n")

# for loop with step in the range()
print("\nUsing a for loop with range and a step:")
for nbr in range(0, 11, 2):
	print(nbr, end=" ")
print("\n")

# for loop with range, counting backwards
print("\nUsing a for loop with range to count backwards:")
for nbr in range(10, 0, -1):
	print(nbr, end=" ")
print("\n")

# for loop to add numbers
print("\nUsing a for loop with range to add up numbers 1 thru 5:")
total = 0
for nbr in range(1,6):
	total += nbr
print("The total of numbers 1 thru 5 is", total)
print("\n")

# for loop to iterate through letters of a string
print("\nUsing a for loop to iterate through letters of a string:")
my_string = "Programming is fun"
for ltr in my_string:
	print(ltr, end="  ")
print()

# nested loop
# for hr in range(1,13):
#     for min in range(1, 60):
#         print(hr,":", min)