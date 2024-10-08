"""
-------------------------------------------------------
Lab 3, Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_queue
from Queue_array import Queue


source = [1, 3, 5, 7, 9]
queue = Queue()

array_to_queue(queue, source)

for values in queue:
    print(values)
