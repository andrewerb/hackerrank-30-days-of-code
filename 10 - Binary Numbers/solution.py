#!/bin/python3

import math
import os
import random
import re
import sys


def consecutive_1_bin(n):
    #counts consecutive 1s in binary conversion of Base10 integer input
    
    log2n = math.log2(n)
    if log2n == int(log2n):
    # equal if log2n (a decimal value) is a whole integer, thus n is a single 1 binary #
        return 1
    else:
        bin_n = bin(n)
        bin_n = (bin_n[2:]) # a string of binary n
        
        current_count = 0
        max_count = 0

        for i in bin_n:
            i = int(i)
            if i == 1:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            elif i == 0:
                current_count = 0
    
    return max_count

if __name__ == '__main__':
    n = int(input())
    print(consecutive_1_bin(n))
