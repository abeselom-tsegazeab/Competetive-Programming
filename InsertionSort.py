import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
            j = n-1
            insertion = arr[-1]
            while j >0 and arr[j-1] > insertion:
                arr[j] = arr[j-1]
                j-=1
                print(*arr)
            arr[j] = insertion
            print(*arr)
 
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
