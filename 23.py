#--------------------27313--------------------
def add1(n):
    return n + 3

def add2(n):
    return n + 4

def multiply(n):
    return n * 2

vars = {
    "a" : add1,
    "b" : add2,
    "c" : multiply,
}

exclude = [20,33]
include = [15,26]

def count(n,included,excluded):
    global exclude
    global include
    if n > 63: return 0
    if n in exclude:
        excluded = False
    if n in include:
        included = True
    if n == 63 and included and excluded: return 1
    a = []
    for funcId in vars.keys():
        a.append(count(vars[funcId](n),included,excluded))
    return sum(a)


print(count(3,False,True))
#--------------------16332--------------------
def plus1(n):
    return n + 1
def plus2(n):
    return n + 2
def multiply2(n):
    return n * 2
funcs = {
    1 : plus1,
    2 : plus2,
    3 : multiply2,
}

def main(start,end,st1,st2):
    if start > end: return 0
    if start == end:
        if st1 and st2:
            return 1
        return 0
    if start == 11:
        st1 = True
    if start == 13:
        st2 = True
    a = []
    for i in funcs:
        a.append(main(funcs[i](start),end,st1,st2))
    return sum(a)
print(main(4,15,False,False))
#---------------------------------------------