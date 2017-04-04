# Day 05 - Loops
#!/bin/python

import sys


n = int(raw_input().strip())

for i in xrange(1,11):
    print n,"x",i,"=",(n*i)
