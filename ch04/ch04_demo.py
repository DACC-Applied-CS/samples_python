##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

def get_values():
	hours = float(input('Enter your hours: '))
	rate = float(input('Enter your rate: '))
	gross = hours * rate
	return hours, rate, gross

def main():
	hrs,rate, gross  = get_values()
	print()
	print(f"{'Hours:':<8}{hrs:6.2f}")
	print(f"{'Rate:':<8}{rate:6.2f}")
	print(f"{'Gross:':<8}{gross:6.2f}")

	
main()