#a pythagorean triplet is a set of natural numbers where a<b<c and a^2+b^2=c^2
#there exist only one pythagorean triplet a+b+c=1000. what is the product axbxc=?

'''
let a = k

k^2+b^2=c^2
k^2 = c^2-b^2 = (c-b)(c+b)

c+b= 1000 - k

c-b=(k^2)/(1000-k)

a = 335, max

'''
product=0

for a in range(1,335):
    c_plus_b=1000-a
    c_minus_b=(a**2)/(1000-a)

    c= int((c_plus_b+c_minus_b)/2)
    b=int(c_plus_b-c)
    if (((a**2)+(b**2)==c**2)and (a<b<c) ):
        product=a*b*c
        break

print("product axbxc=",product)


'''
product axbxc= 31875000
'''