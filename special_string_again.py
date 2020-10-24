#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    arr = [0]*n
    i = 0
    j = 1
    while i < n:
        k = 1
        while  j< n and s[j] == s[i]:
            k+=1
            j+=1
        arr[i] =k
        count += (k*(k+1))>>1
        i =j
        j+=1 

    
    print(arr, count)
    
    for i in range(1, n-1):
        if s[i] == s[i-1]:
            arr[i] = arr[i-1]
        if s[i-1] == s[i+1] and s[i] != s[i-1]:
            count += min(arr[i-1], arr[i+1])

    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
