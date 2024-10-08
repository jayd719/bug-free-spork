"""
-------------------------------------------------------
Assigment 2, Task 5
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import genre_counts, read_movies

fv = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fv)


counts = genre_counts(movies)

print(counts)
