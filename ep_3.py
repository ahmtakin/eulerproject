#problem 3
#find largest prime factor for number 600851475143
import math
bound=int(math.sqrt(600851475143))+1 #holds value for a squared number

def isprime(a):          #tests if an integer is prime
    for i in range(2,a+1):  
        if(a%i==0 and a!=i): #if the int can be divided by another number than itself
            return False
    return True
primes=[]           #holds prime factors      
for i in range(2,bound):
    if(600851475143%i==0):
        if isprime(i):
            primes.append(i)

print(max(primes))  #6857
