#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    assert len(s1) == len(s2)
    l = len(s1) + 1
    #ALERT: avoid usage of shallow list - > arr = [[0]*l]*l 
    arr = [ [None]*l for j in range(l)]
    

    for i in range(l):
        for j in range(l ):
            
            if i == 0 or j ==0:
                arr[i][j] = 0
                
        
            elif s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
                
                
            else:
                
                arr[i][j]  = max(arr[i-1][j], arr[i][j-1])
                
            
    #print(arr)

    return arr[l-1][l-1]







if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
