"""
-------------------------------------------------------
Assignment 7, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-19"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List

# Constants
SEP = "-" * 60
VALUES = [99, 99, 99, 99]
#VALUES = [11, 22, 44, 55]
VALUES2 = [1, 3, 4]
VALUES3 = [4, 5, 6]
# VALUES = [10]


def test_insert():
    print(SEP)
    print(f'Test Insert,Len,Empty')
    source = Sorted_List()
    print('::Before Insert::')
    print(f'Soucrce Len: {len(source)}')
    print(f'Source Empty: {source.is_empty()}')
    print(SEP)
    print('::After Insert::')
    source.insert(2)
    source.insert(4)
    source.insert(3)
    source.insert(1)
    source.insert(9)
    for v in source:
        print(v)
    print(f'Soucrce Len: {len(source)}')
    print(f'Source Empty: {source.is_empty()}')
    print(SEP)
    print('After Remove')
    print(f'Removed: {source.remove(2)}')
    for v in source:
        print(v)
    print(f'Soucrce Len: {len(source)}')
    print(f'Source Empty: {source.is_empty()}')
    print(SEP)
    print('Test Remove Front')
    print(f'Front Removed: {source.remove_front()}')
    for v in source:
        print(v)
    print(f'Soucrce Len: {len(source)}')
    print(f'Source Empty: {source.is_empty()}')
    print(SEP)
    print('Test Remove Many')
    source.insert(7)
    source.insert(6)
    source.insert(6)
    source.insert(6)
    print('::Before Remove Many::')
    for v in source:
        print(v)
    print(f'Soucrce Len: {len(source)}')
    print(f'Source Empty: {source.is_empty()}')
    print(f'Remove Many: {source.remove_many(6)}')
    print('::After Remove Many')
    for v in source:
        print(v)
    print(f'Soucrce Len: {len(source)}')
    print(f'Source Empty: {source.is_empty()}')
    print(SEP)
    print(f'FIND: {source.find(3)}')
    print(SEP)
    print(f'Max: {source.max()}')
    print(f'Mix: {source.min()}')
    print(f'Count 3: {source.count(3)}')
    print(f'Count 3: {source.count(1)}')
    source.insert(3)
    print('After Insert')
    print(f'Count 3: {source.count(3)}')
    print(SEP)
    print('After Adding Duplicates')
    source.insert(4)
    source.insert(4)
    for v in source:
        print(v)
    print('After Clean')
    source.clean()
    for v in source:
        print(v)


def test_intersection():
    print(SEP)
    print('Test Intersection')
    source1 = Sorted_List()
    source2 = Sorted_List()
    target = Sorted_List()
    for v in VALUES:
        source1.insert(v)
    for v in VALUES:
        source2.insert(v)
    target.intersection(source1, source2)
    print(SEP)
    print('After Intersection')
    for v in target:
        print(v)


def test_union():
    print(SEP)
    print('Test Union')
    source1 = Sorted_List()
    source2 = Sorted_List()
    target = Sorted_List()
    for v in VALUES2:
        source1.insert(v)
    for v in VALUES3:
        source2.insert(v)
    target.union(source1, source2)
    print(SEP)
    print('After Union')
    for v in target:
        print(v)


def test_combine():
    print(SEP)
    print('Test Combine')
    source1 = Sorted_List()
    source2 = Sorted_List()
    target = Sorted_List()
    for v in VALUES2:
        source1.insert(v)
    for v in VALUES3:
        source2.insert(v)
    target.combine(source1, source2)
    print(SEP)
    print('After Combine')
    for v in target:
        print(v)


def test_clean():
    print(SEP)
    print('Test Remove')
    source = Sorted_List()
    for values in VALUES:
        source.insert(values)

    source.clean()
    for v in source:
        print(v)
    print(source._count)


def test_remove_front():
    print(SEP)
    print('Test Remove front')
    source = Sorted_List()
    source.insert(99)
    print(len(source))
    source.remove_front()
    print(len(source))


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    print("Test  Sorted List")
    test_insert()
    test_intersection()
    test_union()
    test_combine()
    # test_clean()
    test_remove_front()
