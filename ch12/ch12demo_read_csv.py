##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

import csv

team_dict = {}

########################################
## Read CSV file into a dictionary
#######################################
with open("/workspaces/demos_python/ch12/MLB2022.csv", newline="") as file:
	reader = csv.reader(file)
	next(reader)  # skips the first row (header row)
	for row in reader:
		sub_dict = {}
		sub_dict['Wins'] = row[2]
		sub_dict['Losses'] = row[3]
		team_dict[row[1]] = sub_dict
		

########################################
## Loop through 2D dictionary
#######################################
print(f"{'Team':15}{'Win':>5}{'Loss':>5}")
print("==========================")
for team,stats in team_dict.items():
	print(f"{team:15}", end="")
	for stat, stat_value in stats.items():
		print(f"{stat_value:>5}", end="")
	print()

print("\n")

#####################################
## Lookup a team
#####################################
team = input("Enter a team name: ")

if team in team_dict.keys():
	print(f"{team} won {team_dict[team]['Wins']} games and lost {team_dict[team]['Losses']} games in the 2022 season")
else:
	print("Team not found")
