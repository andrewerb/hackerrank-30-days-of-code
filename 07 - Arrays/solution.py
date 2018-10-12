#!/bin/python3
__author__ = 'Andrew Erb'
# Day 07 - Arrays

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    ## Python 2 leftover code
    # n = int(raw_input().strip())
    # arr = map(int,raw_input().strip().split(' '))

    print(" ".join(map(str, reversed(arr))))
