## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
digit = 0
sum = 0
order = len(str(n))
copy_n = n
while(n > 0):
    digit = n % 10
    sum += digit ** order
    n = n // 10
if(sum == copy_n):
    print('true')
else:
    print('false')
    