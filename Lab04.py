#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1) Ask the user to insert his name and age. Then, calculate his birth year.


# In[4]:


n= input("insert your name")


# In[5]:


x = int(input ("insert your age"))


# In[6]:


from datetime import date


# In[7]:


today = date.today()


# In[8]:


today.year


# In[9]:


a=today.year - x


# In[10]:


print (a)


# In[11]:


#2) Ask the user to insert a text. The program will always answer "yes". The conversation will be closed when the user says "bye".


# In[12]:


text =""
while text!='bye':
    text=input("insert a small text:")
    if text =='bye':
        print()
    else:
        print("yes")


# In[13]:


#3) Create a function for a greeting.


# In[14]:


def greet(name):
    
    print("Hello, " + name + "! Good morning!")


# In[15]:


#4) Call greeting function at the beginning of the conversation.


# In[16]:


greet (n)


# In[ ]:


#5) Improve your chatbot.


# In[ ]:




