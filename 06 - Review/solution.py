__author__ = 'Andrew Erb'
# Day 06 - Review
# author: Andrew Erb
#!/usr/bin/python


# Enter your code here. Read input from STDIN. Print output to STDOUT

 #first input is an int value for how many input strings to expect
for i in range( int(raw_input()) ):
    S = raw_input()
    print(str(S[::2] + ' ' + S[1::2]))
