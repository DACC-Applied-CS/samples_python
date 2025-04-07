
# Person
#	first name
#	last name
#	init (constructor)
#	str
class Person:
	def __init__(self, fname, lname):
		self.first_name = fname
		self.last_name = lname
	
	def __str__(self):
		return f'{self.first_name} {self.last_name}'

# Student
# 	inherits from Person
#	grad year
#	Override init
#	Override str
class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.grad_year = year	

	def __str__(self):
		return super().__str__() + ' graduation year: ' + str(self.grad_year)

# GradStudent
# 	inherit from Student
#	credential
#	Override init
# 	Override str
class Grad_Student(Student):
	def __init__(self, fname, lname, year, credential):
		super().__init__(fname, lname, year)
		self.credential = credential
	
	def __str__(self):
		return super().__str__() + ' credential: ' + self.credential


def main():
	print('\033c\n')  ## clears the screen
	p1 = Person('Jane', 'Doe')
	print(p1)
	print("Object type:", type(p1))
	print()

	s1 = Student('John', 'Doe', 2024)
	print(s1)
	print("Object type:", type(s1))
	print(isinstance(s1,Student))
	print()

	g1 = Grad_Student('Billy', 'Joel', 2025, 'Masters')
	print(g1)
	print("Object type:", type(g1))
	print()

	people = [p1, s1, g1]

	for p in people:
		print()
		print(p)
		print("Object type: ", type(p))
		print("Person?", isinstance(p, Person))
		print("Student? ", isinstance(p, Student))
		print("Grad Student? ", isinstance(p, Grad_Student))

	print("\n")		


main()

