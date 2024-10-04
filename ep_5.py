#2520 can be divided each number in the range 1-10
#what is the smallest number which is evenly divisible for 1-20 range

start=1
def isDivisible(a,x):
    if(a%x==0):
        return True
    else:
        return False
    
def isPrime(x):
    if(x==2):
        return True
    elif(x==1):
        return False
    else:
        for i in range(2,x):
            if(isDivisible(x,i)):
                return False
    return True
                
    
        
def primeFactors(x):
    res=[]
    for i in range(1,x+1):
        if(x==1):
            return 0
        elif(isDivisible(x,i)):
            if(isPrime(i)):
                res.append(i)
                x=x/i

    return res

for i in range(2,20):
    if(isPrime(i)):
        start*=i
    elif(isDivisible(start,i)):
        continue
    else:
        primei=primeFactors(i)
        for j in range(len(primei)):
            if(isDivisible(start*primei[j],i)):
                start*=primei[j]

print(start)
        