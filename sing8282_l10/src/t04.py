"""
-------------------------------------------------------
Lab 10, Task 4
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-30"
-------------------------------------------------------
"""

from test_Sorts_List_linked import test_sort, SIZE
from Sorts_List_linked import Sorts
from test_Sorts_List_linked import SORTS


print(f'n:   {SIZE}       |      Comparisons       | |         Swaps          |')
print('Algorithm      In Order Reversed   Random In Order Reversed   Random')
print('-------------- -------- -------- -------- -------- -------- --------')
for sort in SORTS:
    test_sort(sort[0], sort[1])
