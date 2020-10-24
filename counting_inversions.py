#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):

    n = len(arr)
    if n == 1:
        return 0



    mid = n//2
    h = n - mid
    l = arr[:mid]
    r = arr[mid:]

    count  = inverson(l) + inverson(r)

    p = 0
    k = 0
    i = 0

    for i in range(n):
        if (p < mid) and k < h and  r[k] < l[p]:
            count += mid - p
            arr[i] = r[k]
            i+=1
            k+=1
            continue

        elif p < mid:
            arr[i] = l[p]
            p+=1
        
        else: 
            arr[i] = r[k]
            k+=1
        i+=1

    return count

         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
