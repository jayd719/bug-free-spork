"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      16901XXXX
Email:   sing8282@mylaurier.ca
__updated__ = "2023-06-23"
-------------------------------------------------------
"""
# Imports

n, k = input().split(' ')

sr = input().split(' ')

i = 0
if int(n) > int(k):
    while i < len(sr) and int(sr[int(k)]) <= int(sr[i]) and int(sr[int(k)]) > 0:
        i += 1

print(i)
