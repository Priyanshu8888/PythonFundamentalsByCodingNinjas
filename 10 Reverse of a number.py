#Write Your Code Here
a = int(input())
rev = 0
while(a>0):  
    n = a%10
    rev = rev*10 + n
    a = a//10
    
print(rev)
