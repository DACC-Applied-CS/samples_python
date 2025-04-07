##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

# create a dictionary with income tax rates
state_income_tax = {'IL':4.95, 'IN':3.23, 'OH':3.8,'MI':4.25,'KY':5.00}


# function to get valid decimal user_number
def get_valid_number(min, max, prompt):
	while True:
		user_number = float(input(prompt))
		if user_number < min or user_number > max:
			print('Invalid entry.  Please re-enter.')
			continue
		else:
			return user_number


# function to get valid state
def get_valid_state():
	while True:
		state = input('\nEnter 2 letter state abbreviation: ')
		state = state.upper()
		if state not in state_income_tax:
			print('Invalid state.  Please re-enter')
			continue
		else:
			return state

	
# loop through and display rates
print('\nDisplay all rates:\n--------------------')
for state in state_income_tax:
	print(state, '\t', state_income_tax[state])


# ask user for an hourly pay and calculate annual gross pay
pay_rate = get_valid_number(8.25, 75,'\nEnter your pay rate: ')
HOURS_PER_YEAR = 2080
annual_gross = pay_rate * HOURS_PER_YEAR

# ask the user for a state 
state = get_valid_state()

# calculate their withholding
state_tax = annual_gross * (state_income_tax[state]/100)
pattern = '{}\t${:>8.2f}'

print('\nYour choice - annual withholding:\n---------------------')
print(pattern.format(state, state_tax))


# print all possibilities
print('\nAll choices - annual withholding:\n---------------------')
for item in state_income_tax:
	tax_withheld = state_income_tax[item] / 100 * annual_gross
	print(pattern.format(item, tax_withheld))

# write the dictionary to a binary file
import pickle
with open('states.bin', 'wb') as file:
	pickle.dump(state_income_tax, file)


# read the dictionary from a binary file to a new dictionary
with open('states.bin', 'rb') as file:
	new_dictionary = pickle.load(file)

print('\nNew dicitonary:\n', new_dictionary)
