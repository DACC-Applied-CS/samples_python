##===================================================
## The following clears the screen before code runs
print('\033c\n')
print()
##===================================================

## Task 1:  Create a 2D dictionary with the following 
##	student info:
##	Bob - student ID 001 - 3.5 gpa - 12 credit hours
##	Tom - student ID 002 - 3.0 gpa - 15 credit hours
##	Sue - student ID 003 - 3.4 gpa - 10 credit hours
students = {
	'001': {
		'name':'Bob',
		'gpa':3.5,
		'hrs':12
	},
	'002': {
		'name':'Tom',
		'gpa':3.0,
		'hrs':15
	},
	'003': {
		'name':'Sue',
		'gpa':3.4,
		'hrs':10
	}
}

## Task 2:  Write the loop that will 
##	output the data in a tabular format
##	using f-strings to format

print(f"{'ID':5}{'Name':5}{'GPA':>5}{'Hrs':>5}")
print("====================")

for student,data in students.items():
	print(f"{student:5}",end="")
	for value in data.values():
		print(f"{value:5}",end="")
	print()

print("\n\n")

print(students['001']['gpa'])