n=int(input())
l=0
m=0
for i in range(n):
    for s in range(n-(i+1)):
        print(" ",end="")
    for j in range(i+1):
        print(j+i+1,end="")
    for k in range(i):
        print(l,end="")
        l-=1
    l=m=m+2
    print()