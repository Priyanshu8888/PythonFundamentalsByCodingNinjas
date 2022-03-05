## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while( i <= n):
    spaces = 1
    while(spaces <= n  - i):
        print(' ', end='')
        spaces = spaces + 1
    num = 1
    while(num <= i):
        print(num, end='')
        num = num + 1
    print()
    i = i + 1
        