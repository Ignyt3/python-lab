s=input("Enter the string")

def countvow(a):
    v=0
    for i in s:
        if i in 'aeiouAEIOU':
            v+=1
    return v
    
g=countvow(s)
print(g)
