# Quicksort 1 - Partition

# HackerRank problem solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    brr1=[]
    brr2=[]
    brr3=[]
    p=arr[0]
    brr3.append(p)
    for i in range(1,len(arr)):
        if(p>arr[i]):
            brr1.append(arr[i])
        if(p<arr[i]):
            brr2.append(arr[i])
        if(p==arr[i]):
            brr3.append(arr[i])
    brr1=brr1+brr3+brr2
    return brr1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
