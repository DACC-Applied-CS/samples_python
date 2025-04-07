## The following clears the screen before code runs
print('\033c\n')

## ==============================================================================
## INSTRUCTIONS
## Enter your code below
## Be sure to run the code and capture a screenshot of the code and output
## ==============================================================================

# Task 1) create a dictionary to hold the following witholding rates:
# federal	.20
# state		.0495
# fica		.0725
federal = .20
state = .0495
fica = .0725
# The following function has already been written for you.
# It takes 3 parameters: the minimum, the maximum, 
# 		and the input prompt
# It checks for a valid value - if not valid, it 
# 		asks the user again.  If it is valid, it returns the value
def get_valid_number(min, max, prompt):
  while True:
    user_number = float(input(prompt))
    if user_number < min or user_number > max:
      print('Invalid etnry.  Please re-enter.')
      continue
    else:
      return user_number

# NOTE:  all the rest of the tasks will be written
# 		in the main() function below.  Pay attention to indentation
# 		Put the code beneath the corresponding comment/task
def main():
  pass
  # Task 2) use a for loop to display all the keys and values
  print('\nWithholding rates are:\n======================')
  print('Federal:', federal)
  print('State:  ', state)
  print('FICA:   ', fica)
	
# Task 3) call the get_valid_number() function 
# to ask for the rate.
# Valid values:  between 8.25 and 20.00
  pay_rate = get_valid_number(8.25, 20.00, '\nEnter your pay rate: ')

# Task 4) call the get_valid_number() funtion 
# to ask for the hours.
# Valid values:  between 0 and 40
  hours = get_valid_number(0, 40, '\nEnter your hours: ')

# Task 5) calculate and store the gross pay (hours x rate)
  gross_pay = hours * pay_rate

# Task 6) calculate and store the federal witholding
# Be sure to use the appropriate value from the dictionary
  fed_with = gross_pay * federal

# Task 7) calculate and store the state witholding
# Be sure to use the appropriate value from the dictionary
  state_with = gross_pay * state

# Task 8) calculate and store the fica witholding
#Be sure to use the appropriate value from the dictionary
  fica_with = gross_pay * fica

# Task 9) calculate and store the net amount 
# (gross - federal - state - fica)
  net_pay = gross_pay - fed_with - state_with - fica_with

# Task 10) print out the results
  print("Paycheck info \n=========================")
  print("Gross:   ", gross_pay)
  print("Federal: ", fed_with)
  print("State:   ", state_with)
  print("FICA:    ", fica_with)
  print("=============================")
  print("Net:     ", net_pay)


main()