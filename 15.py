#--------------------9545---------------------
def del10(x):
    return x % 10 == 0
def del26(x):
    return x % 26 == 0
table = []
for A in range(1000):
    fits = True
    for x in range(1000):
        if (del10(x) and del26(x) and (x>=300)) <= (A <= x): continue
        fits = False
        break
    if fits:
        table.append(A)
print(max(table))
#--------------------12247--------------------
def main(x,A):
    return ((x&A) == 0) or ((x&37)!=0) or ((x&12)!=0)
table = []
for A in range(1000):
    state = True
    for x in range(1000):
        if main(x,A): continue
        state = False
        break
    if state:
        table.append(A)
print(max(table))

#--------------------16833--------------------

def main(x,a1,a2):
    P = 250<=x<=730
    Q = 750<=x<=1180
    A = a1<=x<=a2
    return (A and (not(Q))) <= (P or Q)
    

maximum = 0
for a1 in range(250,1180):
    for a2 in range(a1+1,1181):
        if all(main(x,a1,a2) for x in range(1000)):
            maximum = max(maximum,a2-a1)
print(maximum//10)


#---------------------------------------------
#OTHER

#ДЕЛЕНИЕ
# B = [i for i in range(160,181)]

# def del35(x):
#     return x % 35 == 0
# def delA(x,A):
#     return x % A == 0
# def main(x,A):
#     return (x in B) <= (del35(x)<=delA(x,A))

# possibleRange = []

# for A in range(1,1001):
#     checkStatus = True
#     for x in range(1,1000):
#         if main(x,A): continue
#         checkStatus = False
#         break
#     if not checkStatus:continue
#     possibleRange.append(A)
# print(possibleRange)