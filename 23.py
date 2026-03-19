
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