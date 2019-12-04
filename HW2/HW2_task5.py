Number = int(input())
Number_divider = 1 
list_diliver = []
if Number<0:
    print("Это не натуральное число")
while Number_divider<=Number:
    if Number%Number_divider==0:
        list_diliver.append(Number_divider)
    Number_divider+=1
for x in list_diliver:
    print(x,end = ' ')
print()
if len(list_diliver) == 2:
    print("ACHTUNG")