# importing from python library
import sqlite3
import os

# creating a filepath to get to the database
filepath = os.path.join('study_part1.sqlite3')

# connection to the sqlite3 and and feeding the database
connection = sqlite3.connect(filepath)

#
cursor = connection.cursor()

query = '''
CREATE TABLE IF NOT EXISTS profile (
    student_id SERIAL Primary Key,
    student varchar,
    studied varchar, 
    grade int, 
    age int, 
    sex varchar
);
'''

cursor.execute(query)
# connection.commit()

insertion_query = '''
INSERT INTO profile VALUES 
    (1, 'LION-O', 'True', 85, 24, 'Male'),
    (2, 'Cheetara', 'True', 95, 22, 'Female'),
    (3, 'Mumm-Ra', 'False', 65, 153, 'Male'), 
    (4, 'Snarf', 'False', 70, 15, 'Male'), 
    (5, 'Panthro', 'True', 80, 30, 'Male')
'''

cursor.execute(insertion_query)

connection.commit()