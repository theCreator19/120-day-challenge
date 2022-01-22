# Plus Minus

# HackerRankk Problem solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p=0
    ne=0
    z=0
    for i in arr:
        if(i>0):
            p+=1
        elif i<0:
            ne+=1
        else:
            z+=1
    p=p/n
    ne=ne/n
    z/=n
    print('%.6f'%p,'\n%.6f'%ne,'\n%.6f'%z)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
