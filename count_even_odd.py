# find the count of even and odd numbers 
n=[]
even_count=0
odd_count=0
size= int(input("enter the number of elemnts"))
for i in range(size):
    num=int(input("enter the element"))
    n.append(num)
    if num%2==0:
        even_count= even_count+1
    else:
        odd_count= odd_count+1
print("the number of even numbers is",even_count)
print("the number of odd numbers is",odd_count)