def checkPalindrome(num):
    rev = 0
    na = num
    if(num==0):
        return True
    else:
        while(num>0):
            n = num%10
            rev = rev*10 + n
            num = num//10
        if(rev == na):
            return True
        else:
            return False
        

num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
