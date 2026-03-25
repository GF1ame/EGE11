#--------------------20196--------------------
from functools import lru_cache

@lru_cache()
def F(n):
    if n < 110:
        return n
    return n + F(n-1)

for i in range(2025):
    F(i)

print(F(2025)-F(2021))

#--------------------8680---------------------
import sys
sys.setrecursionlimit(1000000)
def H(x):
    if x >= 4040:
        return x
    return x + 4 + H(x+4)

print(H(3)-H(15))
#---------------------------------------------

'''

depending on task, you can either use:

import sys
sys.setrecursionlimit('WHATEVER NUMBER THAT FITS CONDITION')

All your stuff here...

'''

#OTHER
# import sys
# sys.setrecursionlimit(10000)

# @lru_cache()
# def f(n):
#     if n == 1: return 1
#     if n > 1:
#         return n * f(n-1)


# for x in range(2025): f(x)

# print(int((2 * f(2024) + f(2023))/f(2022)))