## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while(i <= n):
    j = 1
    start_char = chr(ord('A') + i - 1 )
    while(j <= i):
        charp = chr(ord(start_char))
        print(charp, end='')
        j = j + 1
    print()
    i = i + 1