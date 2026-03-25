#--------------------14954--------------------
def F(n1,n2,n3,s):
    if n1 >= 20 or n2 >= 20 or n3 >= 20 or n1+n2+n3 >= 25: return s%2==0
    if s == 0: return 0
    f = [F(n1 * 2,n2,n3,s-1),F(n1,n2*2,n3,s-1),F(n1,n2,n3*2,s-1),F(n1 + 2,n2 + 2,n3 + 2,s-1)]
    return any(f) if (s-1)%2 == 0 else all(f)
print("19_14954",[i for i in range(1,19) if F(2,3,i,2)])
print("20_14954",[i for i in range(1,19) if not F(2,3,i,1) and F(2,3,i,3)][:2])
print("21_14954",min([i for i in range(1,19) if not F(2,3,i,2) and F(2,3,i,4)]))

#--------------------11277--------------------

def F(n,m):
    if n >= 268: return m%2==0
    if m == 0: return 0
    h = [F(n+1,m-1),F(n+3,m-1),F(n*4,m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)
print("19_11277",[i for i in range(1,267) if F(i,2)])#replace 'all' to 'any' to get proper answer
print("20_11277",[i for i in range(1,267) if not F(i,1) and F(i,3)][:2])
print("21_11277",min([i for i in range(1,267) if not F(i,2) and F(i,4)]))

#---------------------------------------------

#OTHER
# def f(s1,s2,n):
#     if s1 + s2 <= 69: return n%2==0
#     if n == 0 : return 0
#     k = [f(s1 // 2,s2,n-1),f(s1,s2//2,n-1),f(s1-5,s2 + 2,n-1),f(s1+2,s2-5,n-1)]
#     return any(k) if (n-1) % 2 == 0 else all(k)

# print("19",[i for i in range(51,1000) if f(i,35,2)])
# print("20",[i for i in range(51,1000) if not f(i,35,1) and f(i,35,3)])
# print("21",[i for i in range(51,1000) if not f(i,35,2) and f(i,35,4)])