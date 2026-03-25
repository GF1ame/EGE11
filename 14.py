#---------------------497---------------------
x = 5**94 + 25**49 - 130
string = ""
counter = 0
while x > 0:
    a = x % 5
    if a == 4:
        counter += 1 #1st solution
    string = str(a) + string #2nd solution
    x //= 5
print(string.count("4"),counter)
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