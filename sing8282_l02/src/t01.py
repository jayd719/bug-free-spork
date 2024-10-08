"""
-------------------------------------------------------
Testing Notes
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports

from Stack_array import Stack


s1 = Stack()

# Check if stack is empty
print(s1.is_empty())


s1.push(1)  # add element to stack
s1.push(2)  # add another element to stack

print(s1.is_empty())  # check if stack is empty

s1.push(21)
print(s1.pop())  # pop is the lastest element in stack

print(s1.peek())
