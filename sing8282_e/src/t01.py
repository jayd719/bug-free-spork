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


def timeConversion(s):

    hour = int(s[:2])
    ms = s[2:8]
    if s[-2:] == 'PM':
        if hour < 12:
            hour = 12 + hour
    else:
        if hour >= 12:
            hour = hour - 12

    return f'{hour:02d}{ms}'


def miniMaxSum(arr):
    min_ = 0
    for each in arr:
        min_ += each

    sum_1 = min_
    max_ = 0

    i = 0
    while i < len(arr):
        sum_ = sum_1 - arr[i]
        if sum_ < min_:
            min_ = sum_

        if sum_ > max_:
            max_ = sum_

        i += 1

    print(min_, end=' ')
    print(max_)

    return None


def plusMinus(arr):
    i = 0
    n = len(arr)
    pos_, neg_, zero_ = 0, 0, 0
    while i < n:
        if arr[i] > 0:
            pos_ += 1
        elif arr[i] < 0:
            neg_ += 1
        else:
            zero_ += 1
        i += 1
    print(f'{(pos_ / n):.6f}')
    print(f'{(neg_ / n):.6f}')
    print(f'{(zero_ / n):.6f}')

    return None


def lonelyinteger(a):
    # Write your code here
    value = None
    counter = {}
    i = 0
    while i < len(a):
        if a[i] in counter:
            counter[a[i]] += 1
        else:
            counter[a[i]] = 1
        i += 1

    for m in counter:
        if counter[m] == 1:
            value = m

    return value


def diagonalDifference(arr):
    m = len(arr)
    i = 0
    k = m - 1
    sum_left = 0
    sum_right = 0
    while i < m:
        j = 0
        while j < m:
            if j == i:
                sum_left += arr[i][j]

            if j == k:
                sum_right += arr[i][j]
                k -= 1
            j += 1
        i += 1

    return abs(sum_left - sum_right)


def countingSort(arr):
    n = len(arr)
    interger_array = [0] * 100
    i = 0
    while i < n:
        interger_array[arr[i]] += 1
        i += 1
    i = 0
    while i + 1 < len(interger_array):
        interger_array[i + 1] += interger_array[i]
        i += 1
    places = [0] * n
    i = 0
    while i < n:
        p = interger_array[arr[i]] - 1
        places[p] = arr[i]
        interger_array[arr[i]] -= 1
        i += 1
    return places


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2) - 1
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


def divide_even():
    n = int(input())
    if n % 2 == 0 and n > 2:
        result = 'YES'
    else:
        result = 'NO'
    print(result)


s = '09:05:45AM'

# miniMaxSum([1, 2, 3, 4, 5])
# miniMaxSum([793810624, 895642170, 685903712, 623789054, 468592370])

# plusMinus([-4, 3, -9, 0, 4, 1])

# print(lonelyinteger([1, 1, 2]))

# matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# print(diagonalDifference(matrix))
# Write your code here


# arr = [66, 1, 2, 3, 31, 1, 5, 0]
# print(countingSort(arr))

# findZigZagSequence([2, 3, 5, 1, 4, 6, 7], 7)
# divide_even()
def long_string(text):
    ls = len(text)
    if ls > 10:
        text = f'{text[0]}{ls-2}{text[ls-1]}'
    return text


n = int(input())
while n > 0:
    word = input()
    s = long_string(word)
    n -= 1

    print(s)
