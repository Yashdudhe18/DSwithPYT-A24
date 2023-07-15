#!/usr/bin/env python
# coding: utf-8

# # Dictonary

# Dictonary is a part of Data Structure

# In[1]:


D={"Yashu":25, "Anni":10, "Shardul":30, "Yash":40}


# In[2]:


type(D)


# In[4]:


D


# In[5]:


len(D)


# In[6]:


print(D)


# In[7]:


#Extracting the KEYS from dictonary
D={"Yashu":25, "Anni":10, "Shardul":30, "Yash":40}
D.keys()


# In[8]:


#Extracting the VALUES from dictonary
D={"Yashu":25, "Anni":10, "Shardul":30, "Yash":40}
D.values()


# In[9]:


#Adding new elements to python dictonary
D={"Yashu":25, "Anni":10, "Shardul":30, "Yash":40}
D["Kaushal"]=50
print(D)


# In[11]:


#Changing an existing element to python dictonary
D={"Yashu":25, "Anni":10, "Shardul":30, "Yash":40}
D["Anni"]=20
print(D)


# In[12]:


#Update one dictonary element with another dictonary
D1={"Yashu":25, "Anni":10}
D2={"Shardul":30, "Yash":40}
D1.update(D2)
print(D1)


# In[13]:


#Popping element dictonary in python
D={"Yashu":25, "Anni":10, "Shardul":30, "Yash":40}
D.pop("Yash")
print(D)


# In[17]:


D={"Yashu":25, "Anni":10, "Shardul":30, "Yash":40}
D.pop()
print(D)


# In[ ]:




