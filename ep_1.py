#sum of all mutliples of 3 or 5 below 1000

result=0 #will hold value for sum
for i in range(1000):
    if((i%3==0)or(i%5==0)): #if mod is zero for division to 3 or 5
        result+=i           
print(result)   #233168