#!/usr/bin/env python
# coding: utf-8

# ## Profit or Lost

# In[ ]:


cp=float(input("please enter actual the price: "))
sp=float(input("please enter the selling price: "))

if(cp<sp):
    print("Your profit is: Rs.",sp-cp,"/-")
else:
    print("Don't worry, next time will make profit")


# ## check the given number is positive or negative or Zero

# In[ ]:


num=int(input("Enter the number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("Number is Zero")


# ## Arithmetic operations using if conditions

# In[ ]:


num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
choice=int(input("Enter 1 for Addition,2 for difference, 3 for multiplication, 4 for division: "))
if choice==1:
    print("The addition is: ",num1+num2)
elif choice==2:
    print("The difference is: ",num1-num2)
elif choice==3:
    print("The multiplication is: ",num1*num2)
else:
    print("The division is: ",num1/num2)


# ## Sum of n numbers

# In[ ]:


i=1
n=int(input("Enter the number: "))
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print(sum)


# ## Factorial of a number

# In[1]:


n=int(input("Enter the number"))
f=1
while n>0:
    f=f*n
    n=n-1
print(f)


# ## Leap year or not

# In[ ]:


year=int(input("Enter a year: "))
if (year%4==0  and year%100!=0) or year%400==0 :
    print("This given year is leap")
else:
    print("The given year is not leap")


# ## Grade System

# In[ ]:


grade=int(input("Enter your mark: "))
if grade == 90:
    print ("Grade is A" )
elif grade > 75 and grade < 90:
    print ("Grade is B" )
elif grade < 75 and grade > 65:
    print ("Grade is C" )
elif grade > 50 and grade < 65:
    print ("Grade is D" )
else:
    print ("Fail" )

