n=[]
size=int(input("enter the number of elements"))
for i in range(size):
    num=int(input("enter the elements"))
    n.append(num)
unique=[]
for i in n:
    if i not in unique:
        unique.append(i)
print("the original list is",n)
print("the list without duplicates is ",unique)