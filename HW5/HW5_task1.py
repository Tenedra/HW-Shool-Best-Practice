
def telephone_book() -> list:
    M = int(input())
    keys = [input() for i in range(M)]
    return keys

N = int(input())
contacts = {}
for i in range (N):
    number, k = input().split()
    if k in contacts:
        contacts[k].append(number)
    else: 
        contacts[k] = [number]

for i in (telephone_book()):
    if i in contacts:
        print(*contacts[i])
    else:
        print("нет в списке контактов")

