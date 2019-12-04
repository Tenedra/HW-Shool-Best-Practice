 
subsidy = int(input()) 
acount = int(input())
for i in range(1,subsidy//20):
    for k in range((subsidy - i * 20) // 10 ):
        j = acount - i - k
        if i*20+k*10+j*5 == subsidy:
            print(i,k,j)