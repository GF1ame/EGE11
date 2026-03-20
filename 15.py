#--------------------9545--------------------
def del10(x):
    return x % 10 == 0
def del26(x):
    return x % 26 == 0

for A in range(1000):
    fits = True
    for x in range(1000):
        if (del10(x) and del26(x) and (x>=300)) <= (A <= x): continue
        fits = False
        break
    if fits:
        print(A)
#--------------------------------------------

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