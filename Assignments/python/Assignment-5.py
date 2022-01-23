#!/usr/bin/env python
# coding: utf-8

# ## Sort the dictionary by value

# In[2]:


from operator import itemgetter
dictionary = { 'A':1,'ABC':3,'ABCD':4,'AB':2 }
print("Dictionary: ", dictionary)
sort_dict= dict(sorted(dictionary.items(), key=itemgetter(1))) 
print("Sorted Dictionary by value: ", sort_dict)


# ## Calculator using Oops 

# In[ ]:


class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("The addition is: ",self.num1+self.num2)
    def sub(self):
        print("The difference is: ",self.num1-self.num2)
    def mul(self):
        print("The product is: ",self.num1*self.num2)
    def div(self):
        print("The division is: ",self.num1/self.num2)
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
obj=calculator(n1,n2)
choice=int(input("Enter 1 for add,2 for sub,3 for mul and 4 for division: "))
if choice ==1:
    obj.add()
elif choice ==2:
    obj.sub()
elif choice ==3:
    obj.mul()
elif choice ==4:
    obj.div()
else:
    print("you can enter betweeen 1 and 4")


# ## Print respective month according to number 1 to 12

# In[7]:


n=int(input("Enter the number to find the month: "))
if n<=6:
    if n==1:
        print("January")
    if n==2:
        print("February")
    if n==3:
        print("March")
    if n==4:
        print("April")
    if n==5:
        print("May")
    if n==6:
        print("June")
elif n<=12:
    if n==7:
        print("July")
    if n==8:
        print("Agust")
    if n==9:
        print("September")
    if n==10:
        print("October")
    if n==11:
        print("November")
    if n==12:
        print("December")
else:
    print("Wrong input!. Please enter between 1 to 12")


# ## Print greatest number between three numbers

# In[9]:


x, y, z = input("Enter three values: ").split()
print("The given numbers are: ", x,y,z)
if x>y and x>z:
    print(x,"is the greatest number.")
elif y>x and y>z:
    print(y,"is the greatest number.")
elif z>x and z>y:
    print(z,"is the greatest number.")
else:
    print("2 numbers are having same value")


# ## Print smallest number between three numbers

# In[13]:


x, y, z = input("Enter three values: ").split()
print("The given numbers are: ", x,y,z)
if x<y and x<z:
    print(x,"is the smallest number.")
elif y<x and y<z:
    print(y,"is the smallest number.")
elif z<x and z<y:
    print(z,"is the smallest number.")
else:
    print("2 numbers are having same value")


# ## Table of a number

# In[14]:


n=int(input("Enter the number to create table: "))
for i in range(1,21):
    print(i,"X",n,"=",i*n)


# ## Print even number from 1 to 100

# In[15]:


print("The even numbers from 1 to 100 are: ")
for i in range(1,101):
    if i%2 == 0:
        print(i)


# ## Find the number is prime or not 

# In[19]:


num = int(input("Enter the number to find the prime or not: "))
if num>1:
    for i in range(2,int(num/2)+1):
        if (num%i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")


# ##  Find the reverse of a number

# In[23]:


n = int(input("Enter a number to find reverse: "))
s=str(n)
re=s[::-1]
print("The reverse of",n,"is: ",int(re))


# In[22]:


n = int(input("Enter a number to find reverse: "))
re_n=0
while n!=0:
    digit = n%10
    re_n=re_n*10+digit
    n=n//10
print("The reverse of a number is: ",re_n)
    

