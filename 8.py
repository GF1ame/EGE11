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


    

