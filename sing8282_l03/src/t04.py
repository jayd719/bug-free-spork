"""
-------------------------------------------------------
Lab 3, Task 4
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
from utilities import queue_to_array
from Queue_array import Queue

queue = Queue()

queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.insert(5)


target = []
queue_to_array(queue, target)

print(target)

print('-------')

for values in queue:
    print(values)
