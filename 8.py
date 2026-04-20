from itertools import product
#--------------------2464---------------------
letters = ["Н","И","Ч","Ь","Я"]
vowels = ["И","Я"]
counter = 0

for q,w,e,r,t,y,u in product(letters,repeat=7):
    word = f'{q}{w}{e}{r}{t}{y}{u}'
    glasn = 0
    for i in word:
        if i in vowels:
            glasn += 1
    if glasn != 2: continue
    for i,letter in enumerate(word):
        if not letter in vowels: continue
        valid = True
        if i > 0:
            if not word[i-1] in vowels:continue
            valid = False
            break
        if i < len(word) - 1:
            if not word[i+1] in vowels:continue
            valid = False
            break
    if not valid: continue
    counter += 1
#print(counter)
#--------------------19753--------------------
digits = [0,1,2,3,4,5,6,7,8,9]
chet = [0,2,4,6,8]

amount = 0
for q,w,e,r,t,y in product(digits,repeat = 6):
    digit = f'{q}{w}{e}{r}{t}{y}'
    passed = True
    if len(str(int(digit))) != 6: passed = False
    if int(digit) % 4 != 0:passed = False
    if len(set(digit)) != len(digit): passed = False
    for i in range(len(digit)-1):
        if int(digit[i]) in chet and int(digit[i+1]) in chet:
            passed = False
            break
    if not passed: continue
    amount += 1
#print(amount)

#--------------------23808--------------------
counter = 0
bestPlacement = 0
for i in product(["А","Е","К","Н","О","Т",],repeat = 7):
    counter += 1
    word = "".join(i)
    if word.count("О") == 2 and word.count("К") == 2 and word.count("Т") == 1 and word.count("Е") == 1 and word.count("Н") == 1:
        if counter % 2 == 0: continue
        print(counter)
        bestPlacement = counter
#print(bestPlacement)

#---------------------------------------------


#OTHER

# letters = ["К","А","Б","И","Н","Е","Т"]
# glasn = ["А","И","Е",]
# counter = 0
# for q,w,e,r,t,y,u in product(letters,repeat=7):
#     word = f'{q}{w}{e}{r}{t}{y}{u}'
#     a = set(word)
#     if len(a) != 7: continue
#     if word[-1] in glasn: continue
#     counter += 1
# print(counter)

# letters = ["В","О","З","Д","У","Х"]
# vowels = ["О","У",]
# bad_neighbours = ["В","Х"]
# counter = 0
# for q,w,e,r,t in product(letters,repeat=5):
#     word = f'{q}{w}{e}{r}{t}'
#     if word.count("О") + word.count("У") == 1:
#         valid = True
#         for i,letter in enumerate(word):
#             if letter in vowels:
#                 if i > 0:
#                     if word[i-1] in bad_neighbours:
#                         valid = False
#                         break
#                 if i < len(word) - 1:
#                     if word[i+1] in bad_neighbours:
#                         valid = False
#                         break
#         if not valid: continue
#         counter += 1
# print(counter)

# letters = ["Т","О","Н","Я"]
# vowels = ["О","Я",]
# counter = 0
# for q,w,e in product(letters,repeat=3):
#     word = f'{q}{w}{e}'
#     if len(set(word)) != 3: continue
#     for i, letter in enumerate(word):
#         if not letter in vowels: continue
#         valid = True
#         if i > 0:
#             if not word[i-1] in vowels: continue
#             valid = False
#             break
#         if i < len(word) - 1:
#             if not word[i+1] in vowels: continue
#             valid = False
#             break
#     if not valid: continue
#     counter += 1
# print(counter)


    

