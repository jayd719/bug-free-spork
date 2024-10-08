"""
-------------------------------------------------------
Assignment 9, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from Movie_utilities import read_movies
from Movie import Movie

fh = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fh)
hash_set = Hash_Set(3)
for movie in movies:
    hash_set.insert(movie)

hash_set.debug()
