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

cq = Queue(4)  # circular queue with capacity of 4


# testing
user_input = None
cq.stat()
while user_input != '':
    print('-' * 40)
    user_input = input('Enter I to Insert/ R To Remove from CQ :')
    if user_input == 'I':
        cq.insert(1)
    elif user_input == 'R':
        cq.remove()
    cq.stat()


# for v in cq:
#   print(v)

print(cq.peek())
