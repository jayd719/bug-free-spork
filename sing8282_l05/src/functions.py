"""
-------------------------------------------------------
Custom function Library- Lab 5
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-18"
-------------------------------------------------------
"""
# Imports

ALPHA = 'abcdefghijklmnopqrstuvwzyz'


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = recurse(x - 1, y) + recurse(x, y - 1)
    return ans


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m % n == 0:
        ans = n
    else:
        ans = gcd(n, m % n)
    return ans


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiou"
    count = 0
    if len(s):
        if s[0].lower() in vowels:
            count = 1 + vowel_count(s[1:])
        else:
            count = 0 + vowel_count(s[1:])
    return count


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    ans = 0
    if power == 0:
        if base >= 0:
            ans = 1
        else:
            ans = -1
    elif power == 1:
        ans = base
    elif power < 0:
        base = 1 / base
        power = abs(power)
        ans = base * to_power(base, power - 1)

    else:
        ans = base * to_power(base, power - 1)
    return ans


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    s = s.lower()
    n = len(s)
    palindrome = True
    if n > 1:
        if s[0] not in ALPHA:
            palindrome = is_palindrome(s[1:])
        elif s[n - 1] not in ALPHA:
            palindrome = is_palindrome(s[:n - 1])
        else:

            if s[0] != s[n - 1]:
                palindrome = False
            else:
                palindrome = is_palindrome(s[1:n - 1])
    return palindrome


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list) 
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    m = 0
    new_set = []
    if len(bag):
        if bag[m] not in new_set:
            new_set.append(bag[0])
        bag_to_set(bag[1:])
    return new_set
