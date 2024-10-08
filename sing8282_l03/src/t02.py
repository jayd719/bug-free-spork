"""
-------------------------------------------------------
Lab 3, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
# Imports
from Queue_array import Queue


queue = Queue()

queue.insert(1)
queue.insert(2)
queue.insert(3)

q = queue.remove()

print(q)

value = queue.peek()

print(value)
