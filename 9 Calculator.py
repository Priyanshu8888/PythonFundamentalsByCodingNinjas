# Write your code here
while True:  
    c =int(input())
    if(c == 1):
        a =int(input())
        b=int(input())
        print(a+b)
    elif(c == 2):
        a =int(input())
        b=int(input())
        print(a-b)
    elif(c == 3):
        a =int(input())
        b=int(input())
        print(a*b)
    elif(c == 4):
        a =int(input())
        b=int(input())
        print(int(a/b))
    elif(c == 5):
        a =int(input())
        b=int(input())
        print(a//b)
    elif(c == 6):
        exit()
    else:
        print('Invalid Operation')