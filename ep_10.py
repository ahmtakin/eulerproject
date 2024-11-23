#Find the sum of all the primes below two million.

def isPrime(x):
    if x==0 or x==1:
        return False
    elif x==2:
        return True
    else:
        for i in range(2,x):
            if x%i==0:
                return False
    
    return True
            
    
        
sum=0

for i in range(2,2000000):
    if isPrime(i):
        sum+=i
    


print(sum)        