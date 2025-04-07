class Employee:
	def __init__(self, fn, ln):
		self.first = fn
		self.last = ln

	def getPay(self):
		return 0

	def __str__(self):
		pattern = "Employee: {} {}" 
		return pattern.format(self.first, self.last)


class CommissionEmployee(Employee):
	def __init__(self, fn, ln, cr, gs):
		super().__init__(fn, ln)
		self.comm_rate = cr
		self.gross_sales = gs

	def get_pay(self):
		return self.comm_rate * self.gross_sales

	def __str__(self):
		temp = super().__str__()
		pattern = "{} is commissioned and earned ${:.2f}"
		return pattern.format(temp, self.get_pay())
		
		
class HourlyEmployee(Employee):
	def __init__(self, fn, ln, rt, hr):
		super().__init__(fn, ln)
		self.rate = rt
		self.hours = hr

	def get_pay(self):
		return self.hours * self.rate

	def __str__(self):
		temp = super().__str__()
		pattern = "{} is hourly and earned ${:.2f}"
		return pattern.format(temp, self.get_pay())



def main():
	print('\033c\n')  ## clears the screen
	e1 = Employee("John", "Doe")
	
	ce1 = CommissionEmployee("Jane", "Doe", .06, 5000)
	
	he1 = HourlyEmployee("Darth", "Vader", 10.25, 35)

	employees = [e1, ce1, he1]

	for employee in employees:
		print()
		print(employee)
		print(type(employee))
		print(isinstance(employee, Employee))
	
	
main()