# find the largest and second largest even numbers
n=[]
count=int(input("enter the number of elemnts"))
for i in range(count):
    num=int(input("enter the element"))
    if num%2==0:
        n.append(num)
if len(n)==0:
    print("no even numbers found")
else:
    lar=n[0]
    slar=None
    for i in n:
      if i>lar:
        slar=lar
        lar=i
      elif i<lar:
        if slar is None or i>slar:
            slar=i
    print("largest even number",lar)        
    if slar is None:
     print("no distinct second largest even number")
    else:
     print("second largest even number",slar)
  