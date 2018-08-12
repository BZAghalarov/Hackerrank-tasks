#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    res = 0
    a = list(map(int, input().rstrip().split()))
    for i in a:
        res = res ^ i
    print(res)
