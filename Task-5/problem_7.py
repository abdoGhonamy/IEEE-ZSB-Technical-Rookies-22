#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    lst = []
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            # print(topic[i], topic[j])
            x = int(topic[i]) + int(topic[j])
            # print(x)
            lst.append(len(str(x))-str(x).count("0"))
            # print(lst)
    return [max(lst), lst.count(max(lst))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

