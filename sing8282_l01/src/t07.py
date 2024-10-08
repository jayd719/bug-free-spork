"""
-------------------------------------------------------
Lab 1, Task 7
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-20"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies

fv = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fv)

for each in movies:
    print(each)
    print('-' * 40)
