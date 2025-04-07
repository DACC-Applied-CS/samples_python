##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

#create a list
test_scores = [95, 97, 98, 96, 100]
print("Print whole list", test_scores)

# access a single value
print("Access single value", test_scores[2])

# append a value
test_scores.append(95)
print("After append", test_scores)

# insert a value
test_scores.insert(1,100)
print("After insert", test_scores)

# remove a value
test_scores.remove(100)
print("After removal", test_scores)

# index of a value
print("Index of 98", test_scores.index(98))

# pop - when used without an index, removes (and returns) the last item in the list
removed = test_scores.pop()
print("After pop", test_scores)
print("Value removed", removed)

# length of a list
print("Length", len(test_scores))

# count of how many times value is found
print("Count", test_scores.count(100))

# sort list ascending
test_scores.sort()
print("Sorted", test_scores)

# reverse the order of the lsit
test_scores.reverse()
print("Reversed", test_scores)

# min, max values of a list
print("Min", min(test_scores))
print("Max", max(test_scores))

# sum the values in a list
print("Sum", sum(test_scores))

# randomly chose a value from a list
import random
print("Random", random.choice(test_scores))

# shuffle the list
print("Before shuffle", test_scores)
random.shuffle(test_scores)
print("Afters shuffle",test_scores)

# loop through the items in a list
print("Looping through the scores:")
for score in test_scores:
    print(score)

# Using the in keywords
print("Using in keyword:", end=" ")
if 98 in test_scores:
    print("Value is in list")
else:
    print("Value is not in list")

# parallel list

names = ['Bob','Tom','Bill']
rates = [15.75, 16.00, 15.50]
hours = [20, 25, 15]

for i in range(0, 3):
    print(f"{names[i]} made ${hours[i] * rates[i]:.2f}")
print()

# multi-dimensional list
scores =[[95,100,75],
         [80,70,60],
         [99, 98, 100]]
print("Print 2D list", scores)

print("Looping thru 2D list:")
for r in range(len(scores)):
    for c in range(len(scores[r])):
        print(scores[r][c], end=" | ")
    print() # prints blank row between lists

print()


# unpack a list
num1, num2, num3 = [97, 98, 99]
print("Unpacking", num1, num2, num3)

# function return a list
def ret_multiples(number):
    numbers = []
    for i in range(1, 11):
        numbers.append(i * number)
    return numbers

returned_list = ret_multiples(5)
print("Returned list", returned_list)
print()

# slicing a lit
fruit =['strawberry', 'apple', 'banana','pear', 'peach']

print("Access one item using [3]", fruit[3])
print("Using slicing [2:3]", fruit[2:3])
print("Using slicing [0::2]", fruit[0::2])
print()

# list comprehension
squares = [x**2 for x in range(10)]
print("List comprehension", squares)

names_tuple = ('Bob', 'Tom', 'Bill')
# names_tuple.append('Joe')
# names_tuple.sort()


