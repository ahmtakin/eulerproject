#what is the 10001st prime number given 2 is the first 3 is the second and so on...

def isPrime(x):
    if(x==1 or x==0):
        return False
    elif(x==2):
        return True
    else:
        for i in range(2,x):
            if(x%i==0):
                return False
            
    return True

primes=[]
i=0
while(len(primes)!=10001):
    if(isPrime(i)):
        primes.append(i)
    i+=1

print(primes[-1])
    
#104743