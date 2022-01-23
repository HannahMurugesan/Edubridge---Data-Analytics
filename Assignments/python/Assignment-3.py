#!/usr/bin/env python
# coding: utf-8

# ## Star Pattern 

# In[5]:


for i in range(1,6):
    for j in range(i):
        print('*',end="")
    print()


# In[6]:


for i in range(5,0,-1):
    for j in range(i):
        print('*',end="")
    print()


# ## Number Pattern 

# In[7]:


for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()


# In[8]:


for i in range(5,0,-1):
    for j in range(i):
        print(i,end="")
    print()


# ## Alphabet Pattern

# In[15]:


for i in range(1,6):
    for j in range(i):
        print(chr(64+i),end="")
    print()


# In[17]:


for i in range(5,0,-1):
    for j in range(i):
        print(chr(96+i),end="")
    print()


# ## Pyramid Pattern

# In[20]:


n=int(input("give the range: "))
for i in range(n):
    for j in range(n-i+1):
        print(end=' ')
    for j in range(i+1):
        print(chr(65+i),end=' ')
    print()


# In[21]:


n=int(input("give the range: "))
for i in range(n):
    for j in range(n-i+1):
        print(end=' ')
    for j in range(i+1):
        print(chr(97+i),end=' ')
    print()


# In[23]:


n=int(input("give the range: "))
for i in range(n):
    for j in range(n-i+1):
        print(end=' ')
    for j in range(i+1):
        print(j+1,end=' ')
    print()


# In[ ]:




