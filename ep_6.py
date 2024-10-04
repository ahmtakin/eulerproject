#square of the sums of first 100 natural numbers - sum of the squares of them

sqsum=0
sumsqrt=0
for i in range(101):
    sumsqrt+=i**2
    sqsum+=i
sqsum=sqsum**2
print(sqsum-sumsqrt)
