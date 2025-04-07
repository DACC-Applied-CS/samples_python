##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================
# 1 - import SQLLite3
import sqlite3

# 2 - Display a menu for the user to choose a category
print('''Categories:
1 - Animation
2 - Comedy
3 - History
''')
user_cat = int(input("Enter the number for the category: "))
while user_cat < 1 or user_cat > 3:
	print("Invalid choice.")
	user_cat = int(input("Enter the number for the category: "))

# 3 - connect to the movies database
conn = sqlite3.connect('movies.sqlite')

# 4 - enable use of column names
conn.row_factory = sqlite3.Row

# 5 - create a cursor object
curs = conn.cursor()

# 6 - write the SQL statement
query = '''SELECT Movie.name AS 'movie', \
Category.name AS 'category', year, minutes \
FROM Movie \
JOIN Category ON Movie.CategoryID = Category.CategoryID
WHERE Movie.CategoryID = ?'''

# 7 - excecute the query and return entire result set
curs.execute(query,(user_cat,))
all_movies = curs.fetchall()


# 8 - Display the results
print()
for row in all_movies:
	print("Name:",row['movie'])
	print("Category:",row['category'])
	print("Year:",row['year'])
	print("Minutes:", row['minutes'])
	print()

#9 - Close the connection
conn.close()
