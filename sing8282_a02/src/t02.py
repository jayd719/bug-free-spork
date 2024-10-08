"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_rating, read_movies

fv = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fv)


rmovies = get_by_rating(movies, 8)

print(rmovies)
