# Viral Advertising


# HackerRank Problem solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    s=5
    li=math.floor(s/2)
    cu=math.floor(s/2)
    for i in range(n):
        if(i==n-1):
            return cu
        s=li*3
        li=math.floor(s/2)
        cu=cu+li
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
