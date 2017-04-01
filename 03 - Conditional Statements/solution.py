#Problem 03
#!/bin/python

import sys#


N = int(raw_input().strip())

if (N%2 == 0):
    #even
    if (2<=N<=5):
        print "Not Weird"
    if (6<=N<=20):
        print "Weird"
    if (N>20):
        print "Not Weird"

else:
    #odd
    print "Weird"