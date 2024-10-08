"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-12"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue
# Constants
SEP = "-" * 60
VALUES = [4, 3, 5, 1, 2, 0]
VALUES2 = [4, 3, 5, 1, 2]
VALUES3 = [10, 11, 12, 13]
# VALUES = [10]


def test_is_empty():
    print()
    print(SEP)
    print("Queue: Test Empty")
    source = Queue()
    for v in source:
        print(v)
    print(f"source.is_empty(): {source.is_empty()}")


def test_len():
    print()
    print(SEP)
    print("Queue: Test Len")
    source = Queue()
    for v in source:
        print(v)
    print(f"Len Source: {len(source)}")


def test_full():
    print()
    print(SEP)
    print("Queue: Test Full")
    source = Queue()
    for v in source:
        print(v)
    print(f"Source Full: {source.is_full()}")


def test_insert():
    print()
    print(SEP)
    print("Queue: Test Insert")
    source = Queue()
    for val in VALUES:
        source.insert(val)
    for v in source:
        print(v)
    print(f'Source Len: {len(source)}')
    print(f"source.is_empty(): {source.is_empty()}")


def test_remove():
    print()
    print(SEP)
    print("Queue: Test Remove")
    source = Queue()
    for val in VALUES:
        source.insert(val)
    for v in source:
        print(v)
    print(f'Source Len: {len(source)}')
    print()
    print(SEP)
    print(f'Removed: {source.remove()}')
    print('After Removing')
    for v in source:
        print(v)
    print(f'Source Len: {len(source)}')
    print()
    print(SEP)
    print(f'Removed: {source.remove()}')
    print('After Removing')
    for v in source:
        print(v)
    print(f'Source Len: {len(source)}')
    print(f'PEEK:{source.peek()}')


def test_move():
    print()
    print(SEP)
    print("Queue: Test Move Front To Rear")
    target = Queue()
    source = Queue()
    for val in VALUES:
        target.insert(val)
    print('Initial Target')
    for v in target:
        print(v)
    for val in VALUES2:
        source.insert(val)
    print('Initial Source')
    for v in source:
        print(v)
    print(SEP)
    print('After Move Operation')
    target._move_front_to_rear(source)
    print('Updated Target')
    for v in target:
        print(v)
    print('Updated Source')
    for v in source:
        print(v)


def test_append():
    print()
    print(SEP)
    print("Queue: Test Append")
    target = Queue()
    source = Queue()
    for val in VALUES:
        target.insert(val)
    print('Initial Target')
    for v in target:
        print(v)
    for val in VALUES2:
        source.insert(val)
    print('Initial Source')
    for v in source:
        print(v)
    print(SEP)
    print('After Append')
    target._append_queue(source)
    print('Updated Target')
    for v in target:
        print(v)
    print('Updated Source')
    for v in source:
        print(v)


def test_combine():
    print()
    print(SEP)
    print("Queue: Test COMBINE")
    target = Queue()
    source1 = Queue()
    source2 = Queue()
    for val in VALUES:
        source1.insert(val)
    print('Initial Source1')
    for v in source1:
        print(v)
    for val in VALUES2:
        source2.insert(val)
    print('Initial Source2')
    for v in source2:
        print(v)
    print(SEP)
    target.combine(source1, source2)
    for v in target:
        print(v)
    print()
    print(f'Source 1 is Empty:{source1.is_empty()}')
    print(f'Source 2 is Empty: {source2.is_empty()}')


def test_split_alt():
    print()
    print(SEP)
    print("Queue: Test Split_alt")
    source = Queue()
    for val in VALUES:
        source.insert(val)
    print('Initial Source')
    for v in source:
        print(v)
    target1, target2 = source.split_alt()
    print('Target 1')
    for val in target1:
        print(val)
    print(SEP)
    print('Target 2')
    for val in target2:
        print(val)

    print()
    print(f'Source Empty: {source.is_empty()}')


def test_equal():
    print()
    print(SEP)
    print("Queue: Test equal")
    source1 = Queue()
    source2 = Queue()
    for val in VALUES:
        source1.insert(val)
    print('Initial Source1')
    for v in source1:
        print(v)
    for val in VALUES2:
        source2.insert(val)
    print('Initial Source2')
    for v in source2:
        print(v)
    print(SEP)
    # source2.remove()
    print(source1 == source2)


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    print("Test Queue")
    test_is_empty()
    test_len()
    test_full()
    test_insert()
    test_remove()
    test_move()
    test_append()
    test_combine()
    test_split_alt()
    test_equal()
