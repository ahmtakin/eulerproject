#The sequence of triangle numbers is generated by adding the natural numbers. 
#The first ten terms would be:1,3,6,10,15,21,28,36,45,55
#problem is to find the triangular number with divisors more than 500



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
    res = {}
    for i in range(2, x + 1):
        if x == 1:
            break
        while isDivisible(x, i):
            if isPrime(i):
                if i in res:
                    res[i] += 1
                else:
                    res[i] = 1
                x = x // i
            else:
                continue
    return res

def totalDivisors(x):
    divnum=1
    for _, value in primeFactors(x).items():
        divnum *= (value + 1)

    print("{} has {} divisors".format(x,divnum))
    return divnum
    


triangular=0
inc=0
while True:
    if(totalDivisors(triangular)>500):
        print("{} is a triangular number that has more than 500 divisors".format(triangular))
        break
    else:
        inc+=1
        triangular+=inc


""" result:
..
76576500 has 576 divisors
76576500 is a triangular number that has more than 500 divisors
"""