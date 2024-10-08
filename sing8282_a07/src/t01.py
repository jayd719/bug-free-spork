"""
-------------------------------------------------------
Assignment 7, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-19"
-------------------------------------------------------
"""
# Imports
from List_linked import List

# Constants
SEP = "-" * 60
VALUES = [11, 22, 44, 55]
VALUES2 = [1, 3, 4]
VALUES3 = [4, 5, 6]
# VALUES = [10]


def combine():
    print(SEP)
    print('Test Combine')
    source1 = List()
    source2 = List()
    target = List()
    for v in VALUES2:
        source1.append(v)
    for v in VALUES3:
        source2.append(v)

    target.combine(source1, source2)
    for value in target:
        print(value)
    print(f'Source 1 Empty: {source1.is_empty()}')
    print(f'Source 2 Empty: {source2.is_empty()}')
    print(SEP)
    print(f'Remove Front: {target.remove_front()}')


def test_intersection():
    print(SEP)
    print('Test Intersection')
    source1 = List()
    source2 = List()
    target = List()
    for v in VALUES2:
        source1.append(v)
    for v in VALUES3:
        source2.append(v)

    target.intersection(source1, source2)
    for value in target:
        print(value)


def test_split():
    print(SEP)
    print('Test Split()')
    source1 = List()
    for v in VALUES:
        source1.append(v)
    target1, target2 = source1.split()
    print(SEP)
    print('Target1')
    for v in target1:
        print(v)
    print('Target 2')
    for v in target2:
        print(v)


def test_clean():
    print(SEP)
    print('Test: Clean')
    source = List()
    for v in VALUES:
        source.append(v)
        source.append(v)

    print('Before Clean')
    for v in source:
        print(v)
    print(SEP)
    source.clean()
    print('After Clean')
    for v in source:
        print(v)


def test_union():
    print(SEP)
    print('Test Union')
    source1 = List()
    source2 = List()
    target = List()
    for v in VALUES2:
        source1.append(v)
    for v in VALUES3:
        source2.append(v)

    target.union(source1, source2)
    for value in target:
        print(value)


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    print("Test List")
    combine()
    test_intersection()
    test_split()
    test_clean()
    test_union()
