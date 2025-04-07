##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

# 1) import the sqlite3 library
import sqlite3

# 2) connect to the database
conn = sqlite3.connect('movies.sqlite')

# 3) create a cursor object
curs = conn.cursor()

# 4) create string variable with the query syntax
# and then execute the query 
query = '''SELECT * FROM Movie'''
curs.execute(query)

# 5) fetchone() method of the Cursor object will retrieve one row
one_movie = curs.fetchone()
print(one_movie)
print(type(one_movie))
print()

# 6) fetchall() method of the Cursove object will retrieve all rows
# from the position of the Cursor forward
all_movies = curs.fetchall()
print(all_movies)
print(type(all_movies))
print()
print(type(all_movies[0]))
print()
print(all_movies[0][2]) #first record, third field/column


# 7) close() the connection
conn.close()


