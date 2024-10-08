"""
-------------------------------------------------------
Assignment 5, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-02"
-------------------------------------------------------
"""
# Imports

from List_array import List
from Movie_utilities import read_movies

# read movies data from movies.txt
fh = open('movies.txt', 'r', encoding='utf-8')
movies = read_movies(fh)


source1 = List()  # create List instance 1
source2 = List()  # create List instance 2


# add items to source1:
source1.append(movies[0])
source1.append(movies[1])
source1.append(movies[2])


# add items to source2
source2.append(movies[1])
source2.append(movies[6])
source2.append(movies[7])
source2.append(movies[2])

# print initial stage if Lists
print('Initial State:')
print(f'Source 1:')
for v in source1:
    print(v.title)
print('-' * 40)
print(f'Source 2:')
for v in source2:
    print(v.title)


print(':' * 50, '\n')
# TODO: check if two lists are equal
print(f'Are Two List Equal: {source1 == source2}')

print(':' * 50, '\n')
# TODO: Test Clean()
# add duplicate items of source1
source1.append(movies[2])
source1.append(movies[4])
source1.append(movies[3])
source1.append(movies[2])
source1.append(movies[4])
print('Before Clean:')  # print before cleaning
for value in source1:
    print(value.title)
print('-' * 20)
source1.clean()
print('After Clean:')  # print after running cleaning function
for val in source1:
    print(val.title)


print(':' * 50, '\n')
# TODO: Test Intersection
target = List()  # create another List instance
print('Intersection Of Source 1 And Source 2:')
target.intersection(source1, source2)
for val in target:
    print(val.title)

print(':' * 50, '\n')
# TODO: Test prepend
target.prepend(movies[10])
print('Target after prepending an item.')
for val in target:
    print(val.title)

print(':' * 50, '\n')
# TODO: Test remove front
print(f'Remove Front: {target.remove_front().title}')
print(f'Remove Front: {target.remove_front().title}')

print(':' * 50, '\n')
# TODO: test remove many
source1.append(movies[2])
source1.append(movies[4])
source1.append(movies[3])
source1.append(movies[2])
source1.append(movies[4])
source1.append(movies[5])

# print source1 before running function
print('source 1 before:')
for val in source1:
    print(val.title)
source1.remove_many(movies[2])
print('')
print('Source 1 after:')
for val in source1:
    print(val.title)


print(':' * 50, '\n')
# TODO: test split()
target1, target2 = source1.split()
print('Test Results Split()')
print('Target 1::')
for val in target1:
    print(val.title)
print('')
print('Target 2::')
for val in target2:
    print(val.title)


print(':' * 50, '\n')
# TODO: test split_alts()
target1, target2 = source2.split_alt()
print('Test Results Split()')
print('Target 1::')
for val in target1:
    print(val.title)
print('')
print('Target 2::')
for val in target2:
    print(val.title)


target.union(source1, source2)

print('Nw')
for each in target:
    print(each)
