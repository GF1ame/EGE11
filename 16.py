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
#---------------------------------------------

'''

depending on task, you can either use:

import sys
sys.setrecursionlimit('WHATEVER NUMBER THAT FITS CONDITION')

All your stuff here...

'''