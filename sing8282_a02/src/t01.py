"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_year, read_movies

fv = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fv)


year = 1971
ymovies = get_by_year(movies, year)

print(ymovies)
