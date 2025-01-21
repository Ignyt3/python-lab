a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
c=int(input("Enter 3rd number "))
small=a
big=a
if(b>a):
    if(b>c):
        big=b
if(c>a):
    if(b<c):
        big=c
if(b<a):
    if(b<c):
        small=b
if(c<a):
    if(b>c):
        small=c
    
print("Biggest number is "+str(big))
print("Lowest number is "+str(small))
