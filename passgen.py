#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


import string


# In[ ]:





# In[3]:


def generate_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password


# In[4]:


password = generate_password()


# In[5]:


print(f"Generated password: {password}")


# In[ ]:




