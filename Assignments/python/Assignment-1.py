#!/usr/bin/env python
# coding: utf-8

# ## Arithmetic operations

# In[ ]:


n1=int(input('Enter 1st number:'))
n2=int(input('Enter 2nd number:'))
print('The Sum is: ', n1+n2)
print('The Difference is: ', n1-n2)
print('The Multiplication is: ', n1*n2)
print('The Division is: ', n1/n2)
print('The remainder is: ', n1%n2)


# ## Simple interest

# In[ ]:


Principle=int(input('Enter principle amount'))
Years=int(input('Enter No of years'))
Rate=int(input('Rate of interest'))
SI=(Principle*Years*Rate)/100   #pnr/100
print('The simple Interest is: ',SI)


# ## Swap without 3rd variable

# In[ ]:


x=int(input('Enter a Number: '))
y=int(input('Enter another Number: '))
print('Before Swapping',x,y)
x=x+y
y=x-y
x=x-y
print('After Swapping',x,y)


# ## Swap with 3rd variable 

# In[ ]:


x=int(input('Enter a Number: '))
y=int(input('Enter another Number: '))
print('Before Swapping',x,y)
t=x
x=y
y=t
print('After Swapping',x,y)


# ## Average of 3 students marks 

# In[ ]:


x=int(input('enter mark1:'))
y=int(input('enter mark2:'))
z=int(input('enter mark3:'))
sum=x+y+z
avg=sum/3
print('The average is',avg)


# ## Calculate salary

# In[ ]:


name=input("Name of the employee: ")
basic=float(input('Enter the basic pay'))
da=float(basic*0.05)
hra=float(basic*0.1)
net=float(basic+da+hra)
print('The net salary is:', net)

