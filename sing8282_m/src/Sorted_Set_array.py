"""
-------------------------------------------------------
Array version of the Sorted_Set ADT.
-------------------------------------------------------
Author: Jd Singh
ID:     169018282
Email:  sing8282@mylaurier.ca
__updated__ = "2023-03-04"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class Sorted_Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty set.
        Use: source = Sorted_Set()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            a new Sorted_Set object. (Sorted_Set)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """

        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            the number of values in source. (int)
        -------------------------------------------------------
        """

        return len(self._values)

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in self.
        (Private helper method - used only by other ADT methods.)
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data value (*)
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            i - the index of the only occurrence of key in
                self, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        first = 0
        last = len(self._values) - 1
        index = -1
        while first <= last and index == -1:
            mid = (first + last) // 2
            if self._values[mid] == key:
                index = mid
            else:
                if key < self._values[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return index

    def add(self, value):
        """
        -------------------------------------------------------
        If value does not already exist in source, adds a copy of value
        to source. Returns True if value is added, False otherwise.
        Values in source must remain sorted.
        Use: added = source.add(value)
        -------------------------------------------------------
        Parameters:
            value - data (*)
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            added - True if value added to source, False otherwise. (bool)
        -------------------------------------------------------
        """
        added = False
        if self.is_empty():
            self._values.append(value)
            added = True
        else:
            i = self._binary_search(value)
            if i == -1:
                j = 0
                self._values.append(None)
                while j < len(self._values) - 1 and self._values[j] < value:
                    j += 1
                m = len(self._values) - 1
                while m > j:
                    self._values[m] = self._values[m - 1]
                    m -= 1
                self._values[j] = value
                added = True
        return added

    def discard(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source that matches key.
        Returns None if key not in source.
        Use: value = source.discard(key)
        -------------------------------------------------------
        Parameters:
            key - data key (*)
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            value - the full value matching key, None otherwise. (*)
        -------------------------------------------------------
        """

        i = self._binary_search(key)
        if i == -1:
            value = None
        else:
            value = self._values.pop(i)

        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Returns True if source contains key, False otherwise.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - data key. (*)
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            True if source contains key, False otherwise. (bool)
        -------------------------------------------------------
        """

        i = self._binary_search(key)
        contains = True
        if i == -1:
            contains = False
        return contains

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether source == target are equivalent.
        Values in source and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - Sorted_Set to compare against (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            equals - True if source contains the same values as target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3} == {1,2,3}: True
            {1,2,3} == {1,2,4}: False
            {1,2,3} == {1,2,3,4}: False
        -------------------------------------------------------
        """
        equal = True
        if len(self._values) == len(target._values):
            j = 0
            while j < len(self._values) and equal:
                if self._values[j] != target._values[j]:
                    equal = False
                j += 1
        else:
            equal = False

        return equal

    def issubset(self, target):
        """
        ---------------------------------------------------------
        Tests whether every value in source is also in target.
        Use: subset = source.issubset(target)
        -------------------------------------------------------
        Parameters:
            target - another Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            subset - True if all values in source are also in target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issubset({0,1,2,3,4}): True
            {1,2,3}.issubset({1,2,4,5}): False
        -------------------------------------------------------
        """

        subset = True
        j = 0
        while j < len(self._values) and subset:
            if self._values[j] in target is False:
                subset = False
            j += 1

        return subset

    def isdisjoint(self, target):
        """
        -------------------------------------------------------
        Return True if source has no values in common with target.
        Sorted_Sets are disjoint if and only if their intersection
        is the empty Sorted_Set.
        Use: disjoint = source.isdisjoint(target)
        -------------------------------------------------------
        Parameters:
            target - a Sorted_Set to compare against source. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            disjoint - True if source has no values in common with target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.isdisjoint({4,5,6,7}): True
            {1,2,3}.isdisjoint({1,4,5,6,7}): False
        -------------------------------------------------------
        """
        disjoint = False
        m = self.intersection(target)
        if len(m) == 0:
            disjoint = True

        return disjoint

    def intersection(self, source2):
        """
        -------------------------------------------------------
        Return target with copies of values common to source1 and source2.
        Values may appear only once in target. Values must be sorted.
        Use: target = source1.intersection(source2)
        -------------------------------------------------------
        Parameters:
            source2 - an array-based Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            target - the intersection of source1 and source2. (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.intersection({3,4,5}): {3}
            {1,2,3}.intersection({4,5,6}): {}
        -------------------------------------------------------
        """
        target = Sorted_Set()
        j = 0
        while j < len(self._values):
            if self._values[j] in source2:
                target.add(self._values[j])
            j += 1

        return target

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            value - the next value in the Sorted_Set. (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
