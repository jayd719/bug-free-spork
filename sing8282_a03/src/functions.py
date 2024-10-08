"""
-------------------------------------------------------
Custom Function Library-Assignment 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from enum import Enum

# Constants
ALPHA = 'abcdefghijkmnopqrstuvwxyz'
OPERATORS = "+-*/"

EXIT = 'X'

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1, target2 = Stack(), Stack()
    i = 0
    while source.is_empty() is False:
        if i % 2 == 0:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
        i += 1
    return target1, target2


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """

    string = string.lower()
    string_new = ''
    palindrome = True
    # clean the given string
    for char in string:
        if char in ALPHA:
            string_new += char

    if (len(string_new)) > 0:
        palin = Stack()

        i = 0
        while i < len(string_new):
            palin.push(string_new[i])
            i += 1

        i = 0
        while palindrome and palin.is_empty() is False:
            c = palin.pop()
            if string_new[i] != c:
                palindrome = False
            i += 1
    else:
        palindrome = False
    return palindrome


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    string = string.split(' ')
    stack = Stack()

    for each in string:
        if each not in OPERATORS:
            stack.push(each)
        else:
            right = stack.pop()
            left = stack.pop()
            if each == '-':
                result = float(left) - float(right)
            elif each == '+':
                result = float(left) + float(right)
            elif each == '*':
                result = float(left) * float(right)
            elif each == '/':
                result = float(left) / float(right)
            stack.push(result)

    return stack.pop()


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()
    # create a stack object
    for each in maze['Start']:
        stack.push(each)
    # push start into stack
    path = []  # to keep track of path
    position_visited = []  # keep track position visited
    x = False
    i = 0
    while x is not True and i < len(maze):
        if stack.is_empty() is False:
            key = stack.pop()
            path.append(key)
            if key == EXIT:
                x = True
            else:
                for m in maze[key]:
                    if m not in position_visited:
                        stack.push(m)
                        position_visited.append(m)
        i += 1
    if len(path) == 0 or x is False:
        path = None
    return path


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"

    stack = Stack()
    mirror = True

    if m not in string:
        mirror = MIRRORED.NOT_MIRRORED
    else:
        i = 0
        while mirror and i < len(string)and string[i] != m:
            if string[i] in valid_chars:
                stack.push(string[i])
            else:
                mirror = MIRRORED.INVALID_CHAR
            i += 1

        if len(string[i + 1:]) < i:
            mirror = MIRRORED.TOO_MANY_LEFT
        elif len(string[i + 1:]) > i:
            mirror = MIRRORED.TOO_MANY_RIGHT
        else:
            i += 1
            while mirror and i < len(string)and stack.is_empty() is False:
                c = stack.pop()
                if c != string[i]:
                    mirror = MIRRORED.MISMATCHED
                i += 1

    if mirror == True:
        mirror = MIRRORED.IS_MIRRORED

    return mirror
