n = int(input())
x = (n//2)+1
y = (n//2)

u = 1
while u<=x:
    space = 1
    while space<=(x-u):
        print(" ",end="")
        space = space + 1
    
    star = 1
    while star<=(2*u-1):
        print("*",end="")
        star = star + 1
    print()    
    u = u + 1 

v = y    
while v>=1:
    space = 1
    while space<=(y-v+1):
        print(" ",end="")
        space = space + 1
    star = 1    
    while star<=(2*v-1):
        print("*",end="")
        star = star + 1
    print()
    v = v - 1