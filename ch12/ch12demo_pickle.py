##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

# 2D dictionary, access item
classes = {
	'CSCI-100': {
		'name': 'Intro to C++',
		'credits': 3,
		'book':'Gaddis'
	},
	'CSCI-101': {
		'name':'Intro to Python',
		'credits': 3,
		'book': 'Murach'
	}
}

print('\nPrinting CSCI-101 book author:\n--------------------------- ')
print(classes['CSCI-100']['book'])

# pickling - write to, read from binary
import pickle

with open('classes.bin', 'wb') as file:  #Write to a pickle file
	pickle.dump(classes, file)

with open('classes.bin','rb') as file:  #Read from a pickle file
	new_dictionary = pickle.load(file)

print('\nPrinting new_dictionary:\n--------------------------- ')
print("Printing new dictionary:\n",new_dictionary)
print("Printing old dictionary:\n",classes)

print("\n\n")