import sqlite3


filepath = 'chinook.db'

connection = sqlite3.connect(filepath)

cursor = connection.cursor()

# Find the average invoice total for each customer, return the details for the first 5 ID's

query = '''
SELECT CustomerId, avg (Total)
    FROM invoices
    GROUP BY CustomerId
    LIMIT 5
'''
answer1 = cursor.execute(query).fetchall()
print(' # Find the average invoice total for each customer, return the details for the first 5 ID"s')
print(f'''The average invoice total for the first five ID"S are : \n {answer1}''')


# Return all columns in Customer for the first 5 customers residing in the United States

query = '''
SELECT *
    FROM customers
    WHERE Country = 'USA'
    LIMIT 5
'''

answer2 = cursor.execute(query).fetchall()
print(' \n Return all columns in Customer for the first 5 customers residing in the United States')
print(f'First five customers residing in the United States: \n {answer2}')

# Which employee does not report to anyone?

query = '''
SELECT FirstName, LastName
    FROM employees
    WHERE ReportsTo is NULL
'''

answer3 = cursor.execute(query).fetchall()
print(" \n Which employee does not report to anyone?")
print(f'The employee that does not report to anyone is {answer3[0][0]+" "+answer3[0][1]}.')

# Find the number of unique composers?

query = '''
SELECT count (distinct Composer)
    FROM tracks
'''

answer4 = cursor.execute(query).fetchall()
print(' \n Find the number of unique composer?')
print(f'The number of unique composers are {answer4[0][0]}.')

# How many rows are in the Track table?

query = '''
SELECT count (*)
    FROM tracks
'''

answer5 = cursor.execute(query).fetchall()

print(' \n How many rows are in the Track table?')
print(f'The number of rows in the Track table are {answer5[0][0]}.')


query = '''
SELECT a.Name, al.Title
FROM artists a 
JOIN albums al ON a.ArtistId = al.ArtistId 
JOIN tracks t ON al.AlbumId = t.AlbumId
WHERE a.Name = 'Black Sabbath'
'''