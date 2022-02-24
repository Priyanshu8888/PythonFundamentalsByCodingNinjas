n = int(input())
for i in range(n):
    k = i+1
    for space in range(i):
        print(" ",end="")
    for j in range(n-i):
        print(k,end="")
        k+=1
    print()
    
for i in range(n-1):
    k = n-i-1
    for space in range(n-i-2):
        print(" ",end="")
    for j in range(i+2):
        print(k,end="")
        k+=1
    print()