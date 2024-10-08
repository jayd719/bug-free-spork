"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
# Imports
from functions import is_mirror_stack

mirror = is_mirror_stack("cmc", "abc", "m")
print(mirror)
print(is_mirror_stack("zzxzuzxzz", "xyz", "u"))
print(is_mirror_stack("cmc", "ab", "m"))
print(is_mirror_stack("zzxzxzxzz", "xyz", "u"))
print(is_mirror_stack("zzxzuzx", "xyz", "u"))
