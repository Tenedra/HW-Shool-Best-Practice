
r = int(input()) # число, ближ.знач. в ряде Фиббоначи которого нужно суммировать
count = 0 # счетчик n-значночти числа
x=r
while x!=0:
    x//=10
    count+=1
# определим сколько эллементов ряда нужно вывести
if count==1:  
    a=7
else:
    a = 6*count

f1 = 0; f2 = 1; A = 0
fibonacci_series = []
for i in range(a+1):
    fibonacci_series.append(f1)
    f1,f2= f2,f2+f1

for j in range(len(fibonacci_series)):
    if fibonacci_series[j]>=r: 
        print (fibonacci_series[j]+fibonacci_series[j-1])
        break