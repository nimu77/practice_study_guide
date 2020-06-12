# importing from python library
import sqlite3
import os

# creating a filepath to get to the database
filepath = os.path.join('study_part1.sqlite3')

# connection to the sqlite3 and and feeding the database
connection = sqlite3.connect(filepath)

#
cursor = connection.cursor()

# What is the average age?

query = '''
SELECT AVG (age)
    FROM profile
'''
answer1 = cursor.execute(query).fetchall()
print(' # What is the average age?')
print(f'The average age is {answer1[0][0]}')

# What are name of the female students?

query = '''
SELECT student
    FROM profile
    WHERE sex = 'Female'
'''
answer2 = cursor.execute(query).fetchall()
print(' \n # What are name of the female students??')
print(f'The name of the female student is {answer2[0][0]}.')

# How many students studied?

query = '''
SELECT count (studied)
    FROM profile
    WHERE studied = 'True'
'''
answer3 = cursor.execute(query).fetchall()
print(' \n # How many students studied?')
print(f'The number of students studied are {answer3[0][0]}.')

# Return all students and all columns, sorted by student names in alphabetical order.

query = '''
SELECT *
    FROM profile
    ORDER BY student
'''

answer4 = cursor.execute(query).fetchall()
print(' \n # Return all students and all columns, sorted by student names in alphabetical order')
print(f'The table profile sorted by student \n {answer4}')