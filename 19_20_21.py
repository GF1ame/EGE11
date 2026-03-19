def F(n1,n2,n3,s):
    if n1 >= 20 or n2 >= 20 or n3 >= 20 or n1+n2+n3 >= 25: return s%2==0
    if s == 0: return 0
    f = [F(n1 * 2,n2,n3,s-1),F(n1,n2*2,n3,s-1),F(n1,n2,n3*2,s-1),F(n1 + 2,n2 + 2,n3 + 2,s-1)]
    return any(f) if (s-1)%2 == 0 else all(f)
print("19",[i for i in range(1,19) if F(2,3,i,2)])
print("20",[i for i in range(1,19) if not F(2,3,i,1) and F(2,3,i,3)])
print("21",[i for i in range(1,19) if not F(2,3,i,2) and F(2,3,i,4)])
