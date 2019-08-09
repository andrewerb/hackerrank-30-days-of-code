""" 20 - Sorting
"""


#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numSwaps = 0
is_sorted = False

while (is_sorted is False):
    local_swaps = 0

    for i in range(0, n-1):
        if a[i] > a[i+1]:
            # swap
            temp_a = a[i]
            a[i] = a[i+1]
            a[i+1] = temp_a
            # count
            local_swaps += 1
            numSwaps += 1

    if local_swaps == 0:
        is_sorted = True


firstElement = a[0]
lastElement = a[n-1]

sys.stdout.write("Array is sorted in " + str(numSwaps) + " swaps.\n")
sys.stdout.write("First Element: " + str(firstElement) + "\n")
sys.stdout.write("Last Element: " + str(lastElement))

## The following won't pass HackerRank's tests, because reasons:
# print("Array is sorted in ", numSwaps, " swaps.")
# print("First Element: ", firstElement)
# print("Last Element: ", lastElement, end="")
