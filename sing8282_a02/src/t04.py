"""
-------------------------------------------------------
Assigment 2, Task 4
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_genres, read_movies

fv = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fv)

m = get_by_genres(movies, [3, 4])

print(m)
