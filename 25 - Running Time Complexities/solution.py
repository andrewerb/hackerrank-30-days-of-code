""" Day 25: Running Time and Complexity
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3
import sys
import math


def check_prime(num):
    """ Returns 'Prime' or 'Not prime' for a given positive int.
    """
    if num == 2:  # Allows us to check for n%2 below, and check less in range iterator
        return("Prime")
    if num == 1 or num % 2 == 0:  # 1 is not a prime, nor are even numbers above 2
        return("Not prime")

    sq = int(math.sqrt(num))
    for d in range(3, sq+1, 2):  # start at 3, skip by all even #s
        # A prime int n >1 will have a divisor between 2 and sqrt(n)
        if num % d == 0:
            return("Not prime")

    return("Prime")


T = int(input().strip())
n_list = []
for _ in range(0, T):
    n_list.append(int(input()))
output = []

for n in n_list:
    output.append(check_prime(n))
sys.stdout.write('\n'.join(output))
#print(*n_list, sep='\n')
