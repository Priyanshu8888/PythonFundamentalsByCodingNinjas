## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
print(1)
i = 1
while(i < n):
    j = 0
    while(j <=i):
        if j==i or j==0:
            print(i,end="")
        else:
            print(0,end="")
        j = j + 1    
    print()
    i = i + 1