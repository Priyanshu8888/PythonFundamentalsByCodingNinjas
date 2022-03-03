## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
print(1)
i = 1
while(i < n):
    j = 0
    while(j <i+1):
        if j==i or j==0:
            print(1,end="")
        else:
            print(2,end="")
        j = j + 1    
    print()
    i = i + 1