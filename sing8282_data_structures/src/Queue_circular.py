"""
-------------------------------------------------------
Circular array version of the Queue ADT.
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
Term:    Winter 2020
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy


class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: target = Queue(capacity)
        Use: target = Queue()  # uses default capacity
        -------------------------------------------------------
        Parameters:
            capacity - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert capacity > 0, "Queue size must be > 0"

        self._capacity = capacity
        self._values = [None] * self._capacity
        self._front = None   # queue has no data
        self._rear = 0       # first available index for insertion
        self._count = 0      # number of data items

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """

        return self._rear is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """

        return

    def __eq__(self, target):
        """
        ----------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        equal = True
        if self._count != target._count:
            equal = False

        i = 0
        while equal and i != self._count:
            if self._values[(self._front + i)] != target._values[(target._front + i)]:
                equal = False
            i += 1

        return equal

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: source.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot add to a full queue"

        self._values[self._rear] = deepcopy(value)
        if self._front is None:
            self._front = self._rear

        self._rear += 1
        self._count += 1

        if self._count == self._capacity:
            self._rear = None
        elif self._count != self._capacity and self._rear == self._capacity:
            self._rear = 0

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = source.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        value = deepcopy(self._values[self._front])

        if self._rear is None:
            self._rear = self._front

        if self._front == self._capacity - 1:
            self._front = 0
        else:
            self._front += 1

        self._count -= 1
        if self._count == 0:
            self._front = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"

        value = deepcopy(self._values[self._front])

        return value

    def stat(self):
        """
        -------------------------------------------------------
        To check the status of Rear, Front, Count and full
        Use: source.stat()
        -------------------------------------------------------
        Returns:
           None
       -------------------------------------------------------
       """
        print(f'FRONT: {self._front}')
        print(f'REAR: {self._rear}')
        print(f'COUNT: {self._count}')
        print(f'Full: {self.is_full()}')
        print(f'Empty; {self.is_empty()}')
        print(f'Capacity; {self._capacity}')

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        if self._front is not None:
            # queue is not empty
            j = self._front
            i = 0

            while i < self._count:
                yield self._values[j]
                i += 1
                j = (j + 1) % self._capacity
