from dataclasses import dataclass

@dataclass
class Employee:
	first_name: str
	last_name: str
	hours: float
	__rate: float

	def getGrossPay(self):
		return self.hours * self.__rate

	@property
	def rate(self):
		return self.__rate

	@rate.setter
	def rate(self, rt):
		if rt < 0:
			self.__rate = 15
		else:
			self.__rate = rt

	def __str__(self):
		message = self.first_name + " " + self.last_name
		message += "\nHours:\t" + format(self.hours,'.2f')
		message += "\nRate:\t$" + format(self.__rate,'.2f')
		message += "\nGross:\t$" + format(self.getGrossPay(),'.2f')
		return message


def main():
	print('\033c\n')
	print("\nCreate an Employee with literals:")
	print("=================================")
	e1 = Employee("John", "Doe", 10, 15.25)
	print(e1)

	# Access attributes directly
	print(e1.first_name)
	print(e1.rate)

	e1.rate = -17.25
	print(e1.rate)
	
	# print("\nCreate an Employee from user input:")
	# print("===================================")
	# input_fn = input('Enter the first name: ')
	# input_ln = input('Enter the last name: ')
	# input_hr = float(input('Enter the hours worked: '))
	# input_rt = float(input('Enter the rate of pay: '))
	# print()

	# e2 = Employee(input_fn, input_ln, input_hr, input_rt)
	# print(e2)

	# e3 = Employee(10,12.5,"Tom","Sawyer")
	# print(e3)
	print()

main()