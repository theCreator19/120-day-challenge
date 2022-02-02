# Minimum Absolute Difference in an Array


# HackerRack problem solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    mi=sys.maxsize
    arr=sorted(arr)
    for i in range(n-1):
        s=abs(arr[i]-arr[i+1])
        if s<mi:
            mi=s
            
    return mi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
