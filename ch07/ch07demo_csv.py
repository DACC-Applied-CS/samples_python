##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

import csv

with open('MLB2022.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        print(f"{row[0]:15}{row[1]:15}{row[2]:>10}")
