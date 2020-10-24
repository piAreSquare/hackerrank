#!/bin/python3

import math
import os
import random
import re
import sys




# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    l = len(s)
    hashMap = {}
    #create substring
    subs = [s[i:j] for i in range(l) for j in range(i+1, l+1)]
    for sub in subs:
        # tuples are hashable
        arr = [0]*26
        for x in sub:
            arr[ord(x) - ord('a')] += 1
        arr = tuple(arr)
        if not hashMap.get(arr):
            hashMap[arr] = 0
        hashMap[arr] +=1
    count = 0
    for k,v in hashMap.items():
        count += (v*(v-1))//2 
    
    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
