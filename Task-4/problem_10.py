#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    if min(keyboards) + min(drives) > b:
        return -1
    
    leftover = [b-i for i in keyboards]
    leftover.sort()
    drives.sort()
    
    idx1, idx2 = len(leftover)-1, len(drives)-1
    best = 1000000
    
    while idx1 > -1 and idx2 > -1:
        left, drive = leftover[idx1], drives[idx2]
        x = left - drive
        if x < 0:
            idx2 -= 1
        else:
            best = min(best, x)
            idx1 -= 1
    return b-best

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

