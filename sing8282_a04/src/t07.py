"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

cq1 = Queue(3)  # create circular queue instance 1
cq2 = Queue(3)  # create circular queue instance 2

# add elements to circular queue 1
cq1.insert('ADAM')
cq1.insert('USHER')
cq1.insert('DAVID')

# add elements to circular queue 2
cq2.insert('ADAM')
cq2.insert('DAVID')
cq2.insert('USHER')


print(cq1 == cq2)
