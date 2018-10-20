"""Day 16: Exceptions - String to Integer"""

#!/bin/python3

import sys


S = input().strip()

try:
    print(int(S))
except:
    print("Bad String")
