# Time Conversion

# HackerRank problem solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    t=s.split(":")
    
    if t[2][2]=="P" and t[0]!="12":
        return str(int(t[0])+12)+":"+t[1]+":"+t[2][0:2]
    elif t[2][2]=="A" and t[0]=="12" :
        return "00"+s[2:8]
    elif t[2][2]=="A" and t[0]!="12":
        return s[0:8]
    else:
        return s[0:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
