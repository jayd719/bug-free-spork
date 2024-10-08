"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-16"
-------------------------------------------------------
"""
from Deque_linked import Deque

SEP = "-" * 60
VALUES = [1, 2, 3, 4, 5]
VALUES2 = [4, 3, 5, 1, 2]
VALUES3 = [10, 11, 12, 13]
# VALUES = [10]


def test_is_empty():
    print()
    print(SEP)
    print("Deque: Test Empty")
    source = Deque()
    for v in source:
        print(v)
    print(f"source.is_empty(): {source.is_empty()}")


def test_len():
    print()
    print(SEP)
    print("Queue: Len")
    source = Deque()
    for v in source:
        print(v)
    print(f"len(source): {len(source)}")


def test_insert_front_rear():
    print()
    print(SEP)
    print("Queue: Test Insert Front")
    source = Deque()
    source.insert_rear(4)
    source.insert_front(3)
    source.insert_front(1)
    source.insert_front(2)
    source.insert_rear(6)
    for v in source:
        print(v)


def test_remove():
    print()
    print(SEP)
    print("Queue: Remove")
    source = Deque()
    for val in VALUES:
        source.insert_front(val)
    source.insert_front(11)
    source.insert_rear(10)
    print()
    print(SEP)
    print('BEFORE REMOVE')
    for c in source:
        print(c)
    print(SEP)
    source.remove_front()
    source.remove_rear()
    print('AFTER REMOVE')
    for c in source:
        print(c)
    print(SEP)
    print(f'Source Len:{len(source)}')
    print(SEP)

    source._swap(1, 4)
    print(SEP)
    print("AFTER SWAP")
    for v in source:
        print(v)


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    print("Test Queue")
    test_is_empty()
    test_len()
    test_insert_front_rear()
    test_remove()
