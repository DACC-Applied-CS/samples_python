## The following clears the screen before code runs
import os


## INSTRUCTIONS
## Enter the code from the video in this file.
## Be sure to run the code and capture a screenshot of the code and output


def calc_average(nbr1, nbr2, nbr3):
	average = nbr1 + nbr2 + nbr3 / 3
	return average

def pow_nbr(var1, pwr):
	new_nbr = var1 ** pwr
	return new_nbr

def chg_number(num1):
	num1 = 20

def main():
	os.system('clear')
	num1 = 10
	num2 = 20
	num3 = 30
	calc_average(num1, num2, num3)
	pow_nbr(num1, 3)
	print(num1)
	chg_number(num1)
	print(num1)
	prnt("Hello")


main()

