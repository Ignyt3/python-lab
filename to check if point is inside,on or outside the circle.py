import math
x=float(input("enter the x coordinate of the centre of the circle"))
y=float(input("enter the x coordinate of the centre of the circle"))
r=float(input("enter the radius of the circle"))
a=float(input("enter the x coordinate of the point"))
b=float(input("enter the y coordinate of the point"))
d1=math.sqrt(abs(a**2-x**2))
d2=math.sqrt(abs(b**2-y**2))
z=d1**2+d2**2
if(z>r):
    print("point is outside the circle")
elif(z==r):
    print("point is on the circle")
else:
    print("point is inside the circle")
print(d1,d2)
    
