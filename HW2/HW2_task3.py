x1,x2,y1,y2= map(int, input().split()) 
if abs(x1-y1)==2 and abs(x2-y2)==5 or abs(x1-y1)==5 and abs(x2-y2)==2:
    print("YESSSS!")
else: 
    print("No no")