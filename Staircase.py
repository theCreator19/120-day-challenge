# Staircase

# HackerRank problem solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    i=1
    while(n>0):
        print(" "*(n-1)+"#"*i)
        n-=1
        i+=1


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
