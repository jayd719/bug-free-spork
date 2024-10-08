"""
-------------------------------------------------------
Lab 10, Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-30"
-------------------------------------------------------
"""
# Imports

from test_Sorts_array import SORTS, SIZE
from test_Sorts_array import test_sort

print(f'n:   {SIZE}       |      Comparisons       | |         Swaps          |')
print('Algorithm      In Order Reversed   Random In Order Reversed   Random')
print('-------------- -------- -------- -------- -------- -------- --------')
for sort in SORTS:
    test_sort(sort[0], sort[1])
