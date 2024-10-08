"""
-------------------------------------------------------
Lab 2, Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports

from utilities import stack_to_array

from Stack_array import Stack

stack = Stack()
for m in range(8):
    stack.push(m)

source = []

stack_to_array(stack, source)
