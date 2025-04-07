##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

with open("test.txt",'w') as outfile:
    for i in range(1,11):
        outfile.write(str(i) + "\n")


try:
    sum = 0
    with open("test2.txt",'r') as infile:
        for line in infile:
            sum += int(line)
    print("Sum is", sum)
except:
    print("Error opening file")