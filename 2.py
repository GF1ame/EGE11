# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (not(((not y) <= x)<=w)) or (z<=x)
#                 if f:continue
#                 print(x,y,z,w)
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x or y) and (x <= (not z)) and (not w)
                if not f:continue
                print(x,y,z,w)