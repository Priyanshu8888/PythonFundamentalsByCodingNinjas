## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1 
while(i <= n):
    spaces = 1
    while(spaces <= n - i):
        print(' ', end='')
        spaces = spaces + 1
    star = 1
    while(star <= i):
        print('*', end='')
        star = star + 1
    star = i - 1
    while(star >= 1):
        print('*', end='')
        star = star - 1
    print()
    i = i + 1