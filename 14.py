#---------------------497---------------------
# x = 5**94 + 25**49 - 130
# string = ""
# counter = 0
# while x > 0:
#     a = x % 5
#     if a == 4:
#         counter += 1 #1st solution
#     string = str(a) + string #2nd solution
#     x //= 5
# print(string.count("4"),counter)

#--------------------24048--------------------

Alphabet = { 
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
    "G" : 16,
    "H" : 17,
    "I" : 18,
    "J" : 19,
    "K" : 20,
    "L" : 21,
    "M" : 22,
    "N" : 23,
    "O" : 24,
    "P" : 25,
    "Q" : 26,
    "R" : 27,
    "S" : 28,
    "T" : 29,
    "U" : 30,
    "V" : 31,
    "W" : 32,
}

def custom(num,system):
    newNum = 0
    for i in range(len(num)):
        multiply = len(num) - i - 1
        number = num[i]
        if number in Alphabet:
            number = Alphabet[number]
        number = int(number)
        newNum += (number * system ** multiply)
    return newNum

for i in range(100):
    if custom("KOT",i) + custom("GOLODNI",i) == custom("MEEOW",i) * custom("100",i) - 20194023088:
        print(custom("PURR",i))

#---------------------------------------------

#OTHER
# for x in range(1,1000):idk which one is this xd
#     a = 64**12 - 8**14 + x
#     s = []
#     while a > 0:
#         s = [a%8] + s
#         a //= 8
#     if s.count(7) == 12 and s.count(1) == 1:
#         print(x)

# for n in range(6,20):
#     if (7 ** 500 - int("53",n)) % 6 == 0:
#         print(n)