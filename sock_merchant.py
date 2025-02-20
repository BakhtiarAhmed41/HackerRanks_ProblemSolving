#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    
    for i in range(n):
        num = ar.count(ar[i])
        
        if(i == 0 or ar[i] != ar[i-1]):
            if(num%2==0):
                p = num/2
                pairs += p 
            else:
                num -= 1
                p = num/2
                pairs += p 
        
        else:    
            continue
                
    return int(pairs)    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
