 
a = int(input())
f1 = 0; f2 = 1
fibonacci_series = []
for i in range(a):
    fibonacci_series.append(f1)
    f1,f2= f2,f2+f1
print(*fibonacci_series, sep = ',')