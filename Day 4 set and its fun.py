#!/usr/bin/env python
# coding: utf-8

# In[5]:


#creat a set
s={10,25.5,"Yashu",True}
print(s)


# In[4]:


s   #indexing not possible...unordered


# In[6]:


#duplicate not allowed in set
s={10,25.5,"Yashu",True,10}
print(s)


# In[7]:


s


# In[8]:


len(s)


# In[9]:


type(s)


# In[10]:


s={10,25.5,"Yashu",True,10}
s[0]=30
print(s)


# In[11]:


s={10,25.5,"Yashu",True,10}
s.add("Anni")
print(s)


# In[14]:


s={10,25.5,"Yashu",True,10,"Anni"}
s.remove("Anni")
print(s)


# In[16]:


s={10,20,30}
s.update([1,2,3])
print(s)


# In[21]:


s1={1,2,3}
s2={4,5,6}
s1.union(s2)


# In[22]:


s1={1,2,3}
s2={4,5,3,6}
s1.intersection(s2)


# In[ ]:




