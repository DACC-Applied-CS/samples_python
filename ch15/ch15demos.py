from dataclasses import dataclass

@dataclass
class Person():
	fname: str = "None"
	lname: str = "None"

	def __str__(self):
		return self.fname + ' ' + self.lname

@dataclass
class Student(Person):
	gpa: float = 0.0
	major: str = "None"
	grad_year: int = 0

	def __str__(self):
		temp = super().__str__()
		temp += " GPA: " + str(self.gpa) + " Major: " + self.major + " Grad: " + str(self.grad_year)
		return temp

@dataclass
class Instructor(Person):
	area: str = "None"

	def __str__(self):
		temp = super().__str__()
		temp += " Area: " + self.area
		return temp

def main():
	print('\033c\n')  ## clears the screen
	p1 = Person()
	p2 = Person("John", "Doe")
	p3 = Person("Jane")

	s1 = Student("Jane", "Doe", 3.5,"CS",2023)

	i1 = Instructor("Kathy", "Hunter", "Computer Science")

	people = [p1, p2, p3, s1, i1]

	for p in people:
		print("Printing object:", p)
		print("Type:",type(p))
		print("Person?:", isinstance(p,Person))
		print("Student?:", isinstance(p,Student))
		print("Instructor?:", isinstance(p,Instructor))
		print()


main()