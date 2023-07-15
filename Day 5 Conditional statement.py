#!/usr/bin/env python
# coding: utf-8

# # Conditional Statements

# if /
# if,else /
# nested if /
# ladder if ..

# In[11]:


#Simple IF (if condt is true)
a=5
b=3
if(a>b):
    print("a is greater than b")
   


# In[9]:


print("Enter your name")
x=input()
print("hello " +x)


# In[17]:


#IF-ELSE
a=5
b=3
if(a>b):
    print("a is greater than b")
else :
     print("b is greater than a")
   


# In[18]:


#IF-ELSE
a=5
b=3
if(a<b):
    print("a is greater than b")
else :
     print("b is greater than a")


# In[20]:


print("Enter the percentage")
a=int(input())
if(a>60):
    print("you will be eligiable")
else :
     print("you will no be eligible")


# In[22]:


A=int(input(print("Enter the value of A")))
B=int(input(print("Enter the value of B")))
if(A>B):
     print("A is greater than B")
else :
     print("B is greater than A")


# In[23]:


print("Enter your age")
a=int(input())
if(a<19):
    print("you will be eligiable")
else :
     print("you will no be eligible")


# In[24]:


print("Enter your no")
a=int(input())
if a%2==0:
    print("your no is even")
else :
     print("your no is odd")


# In[25]:


print("Enter your no")
a=int(input())
if a%7==0:
    print("your no is divisible")
else :
     print("your no is not divisible")


# In[28]:


amt=0
a=int(input(print("Enter your electricity unit")))

if a<=100:
    amt=0
if a>100 and a<=200:
    amt=(a-100)*5
if a>200:
    amt=500+(a-100)*10
print("your amt is " ,amt )    


# In[ ]:





# In[ ]:





# In[ ]:




