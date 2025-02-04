s=input("Enter the string")

def lower(s1):
    s2=""
    for i in s1:
        if ord(i)>=65 and ord(i)<=90:
            s2+=chr(ord(i)+32)
        else:
            s2+=i
    print(s2)
lower(s)
def upper(s1):
    s2=""
    for i in s1:
        if ord(i)>=97 and ord(i)<=122:
            s2+=chr(ord(i)-32)
        else:
            s2+=i
    print(s2)
upper(s)
def toggle(s1):
    s2=""
    for i in s1:
        if ord(i)>=97 and ord(i)<=122:
            s2+=chr(ord(i)-32)
        elif ord(i)>=65 and ord(i)<=90:
            s2+=chr(ord(i)+32)
        else:
            s2+=i
    print(s2)
toggle(s)
