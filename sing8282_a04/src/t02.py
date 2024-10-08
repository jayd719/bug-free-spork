"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue


q = Queue()
target = Queue()

target.insert('ADAM')
target.insert('USHER')
target.insert('DAVID')


q.insert('ADAm')
q.insert('USHER')
q.insert('DAVID')
# q.insert(0)

# for v in cq:
#   print(v)


print(q == target)
