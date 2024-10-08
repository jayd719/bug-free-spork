"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze

maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
        'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}

maze1 = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
         'D': [], 'E': ['X', 'F'], 'F': ['G'], 'G': ['C']}

maze2 = {'Start': ['A'], 'A': []}

maze3 = {'Start': ['A'], 'A': ['X', 'B'], 'B': ['C']}

path = stack_maze(maze)
path1 = stack_maze(maze1)
path2 = stack_maze(maze2)
path3 = stack_maze(maze2)

print(path)
print(path1)
print(path2)
print(path3)
