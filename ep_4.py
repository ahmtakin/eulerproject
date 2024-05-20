#find the largest palindrome number which is a product of a and b (a and b are both 3-digit numbers)

import numpy as np
def isPalindrome(x):
    x=str(x)
    xrev=x[::-1]
    if(x==xrev):
        return True
    else:
        return False

a=999
b=999
palindromes=[]

for i in range(900):
    for j in range(900):
        if(isPalindrome((a-i)*(b-j))):
            palindromes.append((a-i)*(b-j))

print(max(palindromes))


