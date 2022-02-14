#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#
def kaprekarNumbers(p, q):
    kn=[]
    for i in range(p,q+1):
        square=i**2
        d=10**len(str(i))
        l=square//d
        r=square%d
        if l+r==i:
            kn.append(i)
    if kn:
        print(*kn)
    else:
        print("INVALID RANGE")
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)

