from itertools import product
#--------------------2464--------------------
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
print(counter)
#--------------------------------------------


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


    

