# for N in range(1000):
#     binary = bin(N)[2:]
#     if N % 2 == 0:
#         binary = "10" + binary
#     else:
#         binary = "1"+binary+"01"
#     r = int(binary,2)
#     if r < 30:
#         print(N)

# import turtle as t

# t.screensize(2000,2000)
# t.tracer(0)
# step = 20

# t.down()

# for i in 1,5:
#     t.forward(37 * step)
#     t.right(90)
#     t.forward(44*step)
#     t.right(90)

# t.up()

# t.backward(18 * step)
# t.right(90)
# t.forward(29*step)
# t.left(90)

# t.down()

# for i in 1,5:
#     t.forward(31 * step)
#     t.right(90)
#     t.forward(35*step)
#     t.right(90)

# t.up()

# for x in range(-50,50):
#     for y in range(-50,50):
#         t.goto(x * step,y*step)
#         t.dot(5,"Red")

# t.exitonclick()

# from itertools import *
# from typing import Callable

# def deco(func : callable):
#     def wrapper():
#         res = func()
#         return res
#     return wrapper

# print("x y w z")
# for x in 0,1:
#     for y in 0,1:
#         for w in 0,1:
#             for z in 0,1:
#                 f = (not(y<=w)) or (x<=z)
#                 if not f:
#                     print(x,y,w,z)
# table = []
# for n in range(20,1000):
#     binary = bin(n)[2:]
#     if n % 2 == 0:
#         binary = "11" + binary[2:] + "0"
#     else:
#         binary = binary + str(binary.count("1") % 2)
#     r = int(binary,2)
#     if r > 154:
#         table.append(n)
# print(min(table))

# import turtle as t

# t.screensize(4000,4000)
# t.tracer(10)
# step = 20

# t.right(90)

# for i in 1,3:
#     t.forward(15*step)
#     t.right(90)
#     t.forward(20*step)
#     t.right(90)

# t.up()
# t.forward(7*step)
# t.right(90)
# t.forward(13*step)
# t.left(90)
# t.down()

# for i in 1,2:
#     t.forward(10*step)
#     t.left(90)
#     t.forward(17*step)
#     t.left(90)
# t.up()

# for x in range(-50,50):
#     for y in range(-50,50):
#         t.goto(x*step,y*step)
#         t.dot(4,"Red")

# t.exitonclick()

# from itertools import product
# counter = 0
# for q,w,e,r,t,y in product([0,1,2,3,4,5,6],repeat=6):
#     a = 3
#     newstring = f'{q}{w}{e}{r}{t}{y}'
#     if int(newstring[0]) % 2 != 0:continue
#     if int(newstring[0])==0:continue
#     if newstring.count("5") != 2:continue
#     counter += 1
# print(counter)

# print((int("324272",23) + int("452562",23))/22)

# def DEL(n,m):
#     return n % m == 0

# list = []
# for x in range(1,10000):
#     f = (not DEL(x,a))<=((not DEL(x,48)) or (not DEL(x,35)))

# def Del( x, D ):
#   return x % D == 0

# def f( x, A ):
#   return (not Del(x,A)) <= ((not Del(x,48)) or (not Del(x,35)))

# for A in range(1,5000):
#   OK = True
#   for x in range(1,5000):
#     if not f(x,A):
#       OK = False
#       break
#   if OK:
#     print(A)

# from functools import *

# @lru_cache(1000000)
# def G(n):
#     if n <= 25:
#         return 2 * (n+1)
#     return G(n-4) + n

# def F(n):
#     return G(n-1) - G(n-5)

# for i in range(0,1000000): G(i)

# print(F(150774))


# def f(s,m):
#     if s >=349: return m%2==0
#     if m == 0: return 0
#     h = [f(s+2,m-1),f(s+3,m-1),f(s*3,m-1)]
#     return any(h) if (m-1)%2==0 else any(h)
# print([s for s in range(1,349) if f(s,2)])
# print([s for s in range(1,348) if not f(s,1) and f(s,3)])
# print([s for s in range(1,348) if not f(s,2) and f(s,4)])
# a = [int(x) for x in open('17.txt')]
# ans = []
# min45 = 1000000

# for i in a:
#     if len(str(i)) != 3 or i % 45 != 0: continue
#     if i < min45:
#         min45 = i

# for i in range(len(a)-1):
#     x,y = a[i],a[i+1]
#     if len(str(x)) == 4 or len(str(y)) == 4:
#         if (x + y) % min45 !=0:continue
#         ans.append(x + y)
# print(len(ans))
# print(min(ans))

# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if w or (y and (not x)) or (not z): continue
#                 print(x,y,z,w)

# table = []

# for i in range(1000):
#     binary = bin(i)[2:]
#     if binary[-1] == "1":
#         binary = "10" + binary[:-2]  + "01"
#     else:
#         binary = "11" + binary[2:] + "1"
#     number = int(binary,2)
#     if i >= 42:
#         table.append(number)
# print(min(table))

# import turtle as t

# t.screensize(2000,2000)
# t.tracer(0)

# step = 20

# for i in range(2):
#     t.forward(12 * step)
#     t.right(90)
#     t.forward(7 * step)
#     t.right(90)
# t.up()
# t.forward(5 * step)
# t.right(90)
# t.down()

# for i in range(2):
#     t.forward(4 * step)
#     t.right(90)
#     t.forward(9 * step)
#     t.right(90)

# t.up()

# for x in range(-20,20):
#     for y in range(-20,20):
#         t.goto(x*step,y*step)
#         t.dot(4,"Red")

# t.exitonclick()

# from itertools import product

# letters = ["Г","И","Н","Р","Ч",]

# a = 1

# for q,w,e,r,t in product(letters,repeat=5):
#     word = f'{q}{w}{e}{r}{t}'
#     if a == 415:
#         print(word)
#         break
#     a += 1

# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (z != y) and (not(x) or y) and w
#                 if not f: continue
#                 print(x,y,z,w)

# changeTable = {
#     "0" : "1",
#     "1" : "2",
#     "2" : "0",
# }
    

# def convert10(number, system):
#     num = number
#     string = ""
#     while num >= system:
#         string += str(num % system)
#         num //= system
#     return (string + str(num))[::-1]
# def duplicate(number):
#     newDigit = ""
#     for digit in number:
#         newDigit += digit * 2
#     return newDigit
# def changeDigits(number):
#     newDigit = ""
#     for i in number:
#         newDigit += changeTable[i]
#     return duplicate(newDigit)

# table = []

# for i in range(1000):
#     tri = convert10(i,3)
#     if i % 3 == 0:
#         tri = duplicate(tri)
#     else:
#         tri = changeDigits(tri)
#     R = int(tri,3)
#     if R > 120:
#         table.append(i)
# print(min(table))


# import turtle as t

# t.screensize(2000,2000)
# t.tracer(0)
# step = 20
# t.down()
# for i in range(3):
#     t.forward(31 * step)
#     t.left(90)
#     t.forward(14 * step)
#     t.left(90)
# t.up()
# t.forward(-4*step)
# t.right(90)
# t.forward(6*step)
# t.left(90)

# t.down()
# for i in range(3):
#     t.forward(11 * step)
#     t.left(90)
#     t.forward(77 * step)
#     t.left(90)
# t.up()

# for x in range(-40,40):
#     for y in range(-40,40):
#         t.goto(x*step,y*step)
#         t.dot(4,"Red")
# t.exitonclick()

# from itertools import product

# sogl = ["В","Ч","Н","С","Т","Ь",]
# letters = ["В","Е","Ч","Н","О","С","Т","Ь",]
# counter = 0
# amountOfWords = 0
# for q,w,e,r,t,y in product(letters,repeat=6):
#     word = f'{q}{w}{e}{r}{t}{y}'
#     counter += 1
#     if counter % 2 == 0: continue
#     if word.count("О") < 2: continue
#     if word[0] in sogl: continue
#     amountOfWords += 1
# print(amountOfWords)

# f = open("9_1.txt")
# counter = 0
# for i in f:
#     array = list(map(int,i.split()))
#     tempDict = {}
#     for x in array:
#         if tempDict.get(x):
#             tempDict[x] += 1
#             continue
#         tempDict[x] = 1
#     if len(tempDict) != 4:
#         continue
#     table = []
#     for x in tempDict.keys():
#         for y in range(tempDict[x]):
#             table.append(x)
#     squaresum = (min(table) + max(table)) ** 2
#     sumsquare = 0
#     for x in (sorted(table))[1:-1]:
#         sumsquare += x ** 2
#     if sumsquare >= squaresum: continue
#     counter += 1
# print(counter)
# a = 0
# for i in range(4096):
#     x = bin(i)[2:]
#     if x.count("1") % 3 == 0: continue
#     print(x)
#     a += 1
# print(a)
# print(int("1" * 42 + "2",5))

# def convert10(number, system):
#     num = number
#     string = ""
#     while num >= system:
#         string += str(num % system)
#         num //= system
#     return (string + str(num))[::-1]
# # print(convert10(16,5))
# bestNumber = 0
# bestAmount = 0
# for x in range(1,2030):
#     th5 = convert10(5**100 - x,5)
#     if th5.count("0") > bestAmount:
#         bestNumber = x
#         bestAmount = th5.count("0")
# print(bestNumber,bestAmount)

# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = x <= (((not z) <= (not y))<=w)
#                 if f:continue
#                 print(x,y,z,w)

# from functools import lru_cache

# import sys
# sys.setrecursionlimit(10000)
# def F(n):
#     if n > 3000:
#         return n
#     return(F(n+2) + 2)

# print(F(40)-F(44))

# f = open("17_1.txt")
# x = [int(i[:-1]) for i in f]

# counter = 0
# bestSumma = -100000000000
# for i in range(0,len(x)-1):
#     pair = x[i:i+2]
#     double = []
#     summa = 0
#     for j in pair:
#         summa += j
#         if len(str(abs(j))) == 2:
#             double.append(j)
#     if len(double) == 0: continue
#     if summa > max(double) : continue
#     counter += 1
#     if summa > bestSumma:
#         bestSumma = summa
# print(counter,bestSumma)


# def f(s,m):
#     if s >=349: return m%2==0
#     if m == 0: return 0
#     h = [f(s+2,m-1),f(s+3,m-1),f(s*3,m-1)]
#     return any(h) if (m-1)%2==0 else any(h)
# print([s for s in range(1,349) if f(s,2)])
# print([s for s in range(1,348) if not f(s,1) and f(s,3)])
# print([s for s in range(1,348) if not f(s,2) and f(s,4)])


# from itertools import product

# letters = ["Л","Е","Г","К","О"]
# poses = []
# counter = 0
# for q,w,e,r,t,y in product(letters,repeat=6):
#     counter += 1
#     word = f'{q}{w}{e}{r}{t}{y}'
#     if word.count("Г") < 2: continue
#     OK = True
#     lastletter = ""
#     for letter in word:
#         if letter == lastletter and letter == "Г":
#             OK = False
#             break
#         lastletter = letter
#     if not OK: continue
#     poses.append(counter)
# print(max(poses))

# f = open("9_2.txt")
# bestChoice = 0
# number = 0
# for x in f:
#     number += 1
#     x = list(map(int,x.split()))
#     tempDict = {}
#     for i in x:
#         if not tempDict.get(i):
#             tempDict[i] = 0
#         tempDict[i] += 1
#     if len(sorted(tempDict.values())) == 5 and sorted(tempDict.values()).count(3) == 1:
#         newList = []
#         for key in tempDict.keys():
#             for j in range(tempDict[key]):
#                 newList.append(key)
#         if sum(sorted(newList)[-2:]) <= sum(sorted(newList)[:-2]): continue
#         print(sorted(newList))
#         bestChoice = number
# print(bestChoice)

# import sys
# sys.setrecursionlimit(10000)

# import math
# import sys
# sys.setrecursionlimit(100000)

# from functools import *

# def f(n):
#     if math.modf(n**0.5)[0]==0:
#         return n ** 0.5
#     return f(n+1) + 1
# print(f(4850)+f(5000))
# @lru_cache(None)
# def g(n):
#     if n == 1: return 1
#     if n > 1: return f(n-1)+2*g(n-1) - n

# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return 2 * f(n-1) + g(n-1) + 2 * n

# for i in range(int(10e3)):f(i)
# for i in range(int(10e3)):g(i)

# print(f(10000)-g(10000)+g(9999)-f(9999))



# def f(n):
#     if n >= 100:
#         a = 1
#         for i in range(1,n+1):
#             a *= i
#         return a
#     else:
#         if n % 2 == 0:
#             return f(n+1)*f(n+2)
#         return (n+2)/f(n+2)
# print(f(10)/f(38))