#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):

    c.sort(reverse=True)

    l = len(c)

    rounds = l//k

    cost = 0

    r = 0
    off = 0

    for i in range(l):
        cost += (r+1)*c[i]

        if (i+ 1) % k ==0:
            r+=1

    return cost

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
