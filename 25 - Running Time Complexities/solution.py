""" Day 25: Running Time and Complexity
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3
import sys
import math


T = int(input().strip())
n_list = []
for _ in range(0, T):
    n_list.append(int(input()))

for i, n in enumerate(n_list):
    if n == 1:
        sys.stdout.write("Not prime")
    else:
        for divisor in range(2, int(math.sqrt(n))+1):
            # A prime int n >1 will have a divisor between 2 and sqrt(n)
            if n % divisor == 0:
                sys.stdout.write("Not prime")
                break
        else:
            sys.stdout.write("Prime")
        if i != T-1:
            sys.stdout.write("\n")
