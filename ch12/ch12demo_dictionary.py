##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================
# Create a dictionary of 3 employees and their pay rates
employees = { "Bob": 15.25, "Tom": 17.75, "Bill": 23.00}

print("\nAccess individual value using [key]:")
print("======================================")
print("Bob makes", employees["Bob"])

employees['Sue'] = 17.25
print(employees)


print("\nFor loop - just the dictionary name:")
print("======================================")

for i in employees:
    print(i)

print("\nFor loop - just the dictionary keys:")
print("======================================")

for i in employees.keys():
    print(i)

print("\nFor loop - just the dictionary values:")
print("======================================")

for i in employees.values():
    print(i)

print("\nFor loop - include key and value:")
print("======================================")
for i in employees.items():
    print(i)

print("\nFor loop - include key/value individually:")
print("===========================================")
for n,v in employees.items():
    print("Name:", n, "\tRate:", v)

