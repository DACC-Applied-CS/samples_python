##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

classes = {'CSCI-100':'Intro to C++',
					 'CSCI-101':'Intro to Python',
					 'CSCI-103':'Intro to Java',
					 'CSCI-200':'Advanced C++',
					 'CSCI-201':'Advanced Python',
					 'CSCI-203': 'Advanced Java'
					}

user = input("Enter a course number: ")
user = user.upper()

if user in classes.keys():
	print('The class is', classes[user])
else:
	print('That class was not found')

# Instructions:
# 1) Create a list with the following key/value pairs:
# 		KEY:				VALUE:
# 		CSCI-100		Intro to C++
# 		CSCI-101		Intro to Python
# 		CSCI-103		Intro to Java
# 		CSCI-200		Advanced C++
# 		CSCI-201		Advanced Python
# 		CSCI-203		Advanced Java
# 2) Prompt the user for a class code. User the appropriate
#			string method to convert to uppercase in case they enter
#			the class code in lower case
#	3) Look up the value they entered.  If it is in the dictionary,
#			then return the corresponding class name
#			If it is not, tell them it was not found.

