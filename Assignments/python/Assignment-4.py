#!/usr/bin/env python
# coding: utf-8

# ##  Find the factors of a number

# In[ ]:


def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
num = int(input("Enter the number to find factors: "))
print_factors(num)


# ## Fibonacci Series

# In[ ]:


n=int(input("Enter a number to find fibonacci: "))
n1=0
n2=1
count=0
while count<n:
    print(n1)
    n3=n2+n1
    n1=n2
    n2=n3
    count+=1


# ## Program to find the roots of a quadratic equation

# In[ ]:


import math
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
d=(b**2)-(4*a*c)
if d>0:
    R1=(-b+math.sqrt(d)/(2*a))
    R2=(-b-math.sqrt(d)/(2*a))
    print("Two distinct real roots:\nRoot 1 and Root2 are:\n",(R1,R2))
elif d==0:
    R1=R2=(-b/(2*a))
    print("Two equal and real roots:\nRoot1  and Root2 are:\n",(R1,R2))
elif d<0:
    R1=R2=(-b/(2*a))
    imaginary=math.sqrt((-d)/(2*a))
    print("Two distinct complex roots:\nRoot1 and Root2 are:\n",(R1+imaginary,R2-imaginary))


# ## 
