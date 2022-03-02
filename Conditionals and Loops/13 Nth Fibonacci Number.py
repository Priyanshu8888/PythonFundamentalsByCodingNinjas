## Read input as specified in the question.
## Print output as specified in the question.
x = int(input())
n1, n2 = 0, 1
count = 0

if x <= 0:
    exit()
elif x == 1:
    print(n2)
else:
    while count < x:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print(n1)