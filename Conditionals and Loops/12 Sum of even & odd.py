## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
a = int(input())
x = 0
y = 0
while(a>0):
    n = a%10
    if(n%2 == 0 ):
        x = x + n
    else:
        y = y + n
    a = a//10
print( x, y)
        