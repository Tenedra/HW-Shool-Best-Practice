def b_day_book() -> list:
    M = int(input())
    keys = [input() for i in range(M)]
    return keys

N = int(input())
dr = {}
for i in range (N):
    name,day,month = input().split()
    if month in dr:
        dr[month].append([name,day])
    else: 
        dr[month] = [[name, day]]

a = (b_day_book())
for key in a:
    if key in dr:
        a = sorted(dr[key], key = lambda x: (int(x[1]), x[0]))
        s = ''
        for x in a:
            s+=' '.join(x) + ' '
        print(s)
    else:
        print("ФУХ НИКОГО НЕТ")