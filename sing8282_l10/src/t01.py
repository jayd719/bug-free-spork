"""
-------------------------------------------------------
Lab 10, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-30"
-------------------------------------------------------
"""
# Imports

from test_Sorts_array import create_sorted, create_reversed, create_randoms
from test_Sorts_array import test_sort
from Sorts_array import Sorts
SEP = '-' * 40


values = create_randoms()


sort = test_sort('Insertion Sort', Sorts.insertion_sort)
