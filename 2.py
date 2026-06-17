#--------------------2664--------------------
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x or y) and (x <= (not z)) and (not w)
                if not f:continue
                print(x,y,z,w)
#--------------------5867--------------------
from itertools import *

def f(x,y,w,z):
    return (w == (z<=x)) and y

for a1,a2,a3,a4,a5 in product([0,1],repeat=5):
    table = [(a1,0,a2,0),(1,a3,1,1),(a4,a5,0,0)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,r))) for r in table]==[1,0,1]:
                print(p)

#--------------------23725-------------------

print("m e o w")
for m in range(2):
    for e in range(2):
        for o in range(2):
            for w in range(2):
                f = (m <= e) or (o == e) and w
                if f:continue
                print(m,e,o,w)

#--------------------23725-------------------

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not((w or not(y)) and x) or (y == z)
                if f:continue
                print(x,y,z,w)

#--------------------18162-------------------

print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((a <= b) == c) or d
                if f: continue
                print(a,b,c,d)

#--------------------29553-------------------
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not((x<=w) <= (w == z)) and y
                if not f: continue
                print(x,y,z,w)
#--------------------------------------------