## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
#start_char = chr(ord('E') + i -1)
while(i <= n):
    j = 1
    p = n
    while(j <= i):
        charp = chr(ord('A') + p -i)
        print(charp, end='')
        j = j + 1
        p = p + 1
    print()
    i = i + 1
    