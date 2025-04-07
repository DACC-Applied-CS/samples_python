##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================


my_file = open('sample.txt','w')

for i in range(1,6):
    my_file.write(str(i) + "\n")

my_file.close()

###############################
read_file = open('sample.txt','r')

total = 0

for line in read_file:
    total += int(line)

print(total)

read_file.close()
