A, B = map(int, input().split())
def amount(A, B):
    c = 0
    for i in range(A, B+1, 1):
        c += i
        return(c)
if A<B:
    print(amount(A,B))
else:
    A,B = B,A
    print(amount(A,B))