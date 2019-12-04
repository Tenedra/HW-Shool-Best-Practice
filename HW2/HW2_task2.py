
A, B = map(float, input().split()) 
s = input()
if s == "+": print(A+B)
elif s== "-": print(A-B)
elif s == "*": print(A*B)
elif s == "/" and B==0: print("ЫЫЫЫЫЫ")
elif s=="/" and B!=0: print(A/B)
else:
    print("ЫЫЫЫЫЫ")