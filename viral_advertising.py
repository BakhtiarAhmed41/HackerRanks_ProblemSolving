#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    cumulative = 0
    likes = 0
    shared = 5
    
    
    for i in range(n):
        
        likes = math.floor(shared/2)
        cumulative += likes
        shared = likes*3
        
    
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
