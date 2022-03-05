## Read input as specified in the question.
## Print output as specified in the question.
row = int(input())

for i in range(1, row+1):

    for j in range(1, row+1-i):
        print(' ', end='')

    for j in range(i, 0, -1):
        print(j, end='')

    for j in range(2, i+1):
        print(j, end='')

    print()