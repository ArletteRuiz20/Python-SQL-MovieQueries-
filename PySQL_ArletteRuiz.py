
from cis2010utils4 import StartHere, EndHere, runsql
##from colorama import Fore
import pandas as pd
import sqlite3
############################################################################
#
# Task 2a
StartHere( "Arlette Ruiz", "S12", "Fall 2024")
#
#
# Open up the database  ########## Do not modify these instructions#########
db_name =  "Movies2023x4.db"
db_conn = sqlite3.connect(db_name)
sqltxt = "pragma table_info('movies')" ; t1 = pd.read_sql(sqltxt, db_conn) ; print("movies table\n", t1)
sqltxt = "pragma table_info('crew')" ; t2 = pd.read_sql(sqltxt, db_conn) ; print("crew table\n", t2)
sqltxt = "pragma table_info('lang')" ; t3 = pd.read_sql(sqltxt, db_conn) ; print("lang table\n", t3)
sqltxt = "pragma table_info('genre')" ; t4 = pd.read_sql(sqltxt, db_conn) ; print("genre table\n", t4)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
############################################################################
#
#
# Task w3a
sqlw3a = """
SELECT year FROM movies
"""
w3a = runsql( sqlw3a, db_conn, False)

#
# Task w3c
sqlw3c = """
SELECT DISTINCT year FROM movies
"""
w3c = runsql( sqlw3c, db_conn, False)

#
# Task w4a
sqlw4a = """
SELECT year, title, revenue
FROM movies
WHERE title = 'Barbie'
"""
w4a = runsql( sqlw4a, db_conn, True)

#
# Task w4b
sqlw4b = """
SELECT year, title, revenue
FROM movies
WHERE title LIKE '%Barbie%'
"""
w4b = runsql( sqlw4b, db_conn, True)

#
# Task w4c
sqlw4c = """
SELECT year, title, revenue
FROM movies
WHERE title LIKE '%indiana jones%'
ORDER BY revenue
"""
w4c = runsql( sqlw4c, db_conn, True)

#
# Task w5a  
sqlw5a = """
SELECT year, title, revenue, actor
FROM movies
WHERE title LIKE '%indiana jones%'
ORDER BY revenue
"""
#w5a = runsql( sqlw5a, db_conn, False)

#
# Task w5b
sqlw5b = """
SELECT * FROM crew
"""
w5b = runsql( sqlw5b, db_conn, False)

# Task w5c
sqlw5c = """
SELECT year, title, actor
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE title LIKE '%indiana jones%'
"""
w5c = runsql( sqlw5c, db_conn, False)

# Task w5d
sqlw5d = """
SELECT year, title, actor, MAX(revenue)
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE title LIKE '%indiana jones%' AND actor = 'John Rhys-Davies'
"""
w5d = runsql( sqlw5d, db_conn, True)
#AND actor LIKE '%Banderas%'

#
# Task w6a
sqlw6a = """
SELECT year, title, actor, MAX(revenue)
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE actor = 'Zoe Saldana'
"""
w6a = runsql( sqlw6a, db_conn, True)

#
# Task w6b
sqlw6b = """
SELECT actor, SUM(revenue)
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE actor = 'Zoe Saldana'
"""
w6b = runsql( sqlw6b, db_conn, True)

#
# Task w7a
sqlw7a = """
SELECT DISTINCT genre
FROM movies JOIN genre ON movies.title = genre.title
WHERE movies.title LIKE '%Avatar%'
"""
w7a = runsql( sqlw7a, db_conn, False)

#
# Task w7c
sqlw7c = """
SELECT DISTINCT g.genre
FROM movies m
JOIN genre g ON m.title = g.title
WHERE m.title LIKE '%Indiana Jones%';

"""
w7c = runsql( sqlw7c, db_conn, False)


# Workshop END
#

pd.set_option('display.max_rows', 32)
#
# S12ccq Q5
sqlcc5 = """
SELECT title, COUNT(*)
FROM movies
WHERE title LIKE 'Frozen%'
"""
cc5 = runsql( sqlcc5, db_conn, False)

#
# S12ccq Q6
sqlcc6 = """
SELECT title, COUNT(*)
FROM movies
WHERE title LIKE 'Frozen%' AND budget > '100000000.0'
"""
cc6 = runsql( sqlcc6, db_conn, False)

#
# S12ccq Q7
sqlcc7 = """
SELECT title, actor
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE title LIKE 'Frozen%' AND actor = 'Idina Menzel'
"""
cc7 = runsql( sqlcc7, db_conn, False)

#
# S12ccq Q8
sqlcc8 = """
SELECT DISTINCT g.genre
FROM movies m
JOIN genre g ON m.title = g.title
WHERE m.title LIKE '%Frozen'
"""
cc8 = runsql( sqlcc8, db_conn, False)

#
# S12ccq Q9
sqlcc9 = """
SELECT title
FROM movies
WHERE title LIKE 'Spider%'
"""
cc9 = runsql( sqlcc9, db_conn, False)

#
# S12ccq Q10
sqlcc10 = """
SELECT c.actor
FROM movies m
JOIN crew c ON m.mid = c.movieID
WHERE m.title = 'Spider-Man' AND m.year = 2002
"""
cc10 = runsql( sqlcc10, db_conn, False)

#
# S12ccq Q11
sqlcc11 = """
SELECT DISTINCT g.genre
FROM movies m
JOIN genre g ON m.title = g.title
WHERE m.title = 'Black Panther' AND m.year = 2018
"""
cc11 = runsql( sqlcc11, db_conn, False)

#
# S12ccq Q12
sqlcc12 = """
SELECT DISTINCT movies.title
FROM movies 
JOIN genre ON movies.title = genre.title
WHERE genre.genre = 'Science Fiction' AND movies.title LIKE '%Shrek%'
"""
cc12 = runsql( sqlcc12, db_conn, False)

#
# S12ccq Q13
sqlcc13 = """
SELECT movies.title
FROM movies
WHERE movies.title LIKE '%Shrek%' AND movies.year = 2010
"""
cc13 = runsql( sqlcc13, db_conn, False)



# Individual Challenge
#
# S12icq Q2
sqlic2 = """
SELECT *
FROM lang
"""
ic2 = runsql( sqlic2, db_conn, False)

#
# S12icq Q3
sqlic3 = """
SELECT lang.orig_lang
FROM movies
JOIN lang ON movies.mid = lang.mid
WHERE movies.title = 'The Pope: Answers'
"""
ic3 = runsql( sqlic3, db_conn, False)

#
# S12icq Q4
sqlic4 = """
SELECT MAX(movies.score) AS max_score
FROM movies
JOIN crew ON movies.mid = crew.movieID
WHERE crew.actor = 'Whoopi Goldberg'
"""
ic4 = runsql( sqlic4, db_conn, False)

#
# S12icq Q5
sqlic5 = """
SELECT MAX(movies.year) AS latest_release
FROM movies
WHERE movies.title = 'Titanic'
"""
ic5 = runsql( sqlic5, db_conn, False)

#
# S12icq Q6
sqlic6 = """
SELECT lang.country
FROM movies
JOIN lang ON movies.mid = lang.mid
WHERE movies.title = 'Stromboli'
"""
ic6 = runsql( sqlic6, db_conn, False)

#
# S12icq Q7
sqlic7 = """
SELECT genre.genre
FROM movies
JOIN genre ON movies.title = genre.title
WHERE movies.title = 'Tenet' AND movies.year = 2020
"""
ic7 = runsql( sqlic7, db_conn, False)


###########################################################
#
#Individual Challenge: End
db_conn.close()
EndHere(globals())
#exit();
############################################################
#Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$>#UFWQJYYJ%WZN_%4ZXJWX4FWQJYYJWZN_lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
