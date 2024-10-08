"""
-------------------------------------------------------
Lab 9, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
# Imports

from functions import hash_table
from Movie_utilities import read_movies
from Movie import Movie

fh = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fh)

hash_table(7, movies)
