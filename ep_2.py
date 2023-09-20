#problem2
#sum of fibonacci sequence even valued terms which are below 4 million
result=0 #holds solution
fib1=1 #defining variables for initial terms
fib2=1 
next_term=0 #holds current term
while(fib2<4000000): 
    next_term=fib1+fib2 #calculates new term
    if(next_term%2==0): #if it is even
        result+=next_term #adds to the sum
    fib1=fib2         
    fib2=next_term
print(result) #4613732