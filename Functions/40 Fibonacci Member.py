def checkMember(n):
    if(n==0 or n==1 or n==2):
      return True
    a=0
    b=1
    while(b<n):
        c=a+b
        a=b
        b=c
    if(b==n):
      return True
    return False


n=int(input())

isfibonacci = checkMember(n)
if(isfibonacci):
    print("true")
else:
    print("false")