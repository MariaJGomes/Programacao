#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Read the file. The file may be stored in a local folder on in the internet.


# In[3]:


import requests
url='https://raw.githubusercontent.com/masterfloss/data/main/jobs.txt'
response = requests.get (url)
speech = response.text


# In[4]:


print (speech)


# In[5]:


#2. What is the type of data stored into the variable speech.


# In[6]:


type (speech)


# In[7]:


#3. Remove simbols that are not useful. Sugestion: use replace method.


# In[8]:


x = speech.replace ('.', ' ')


# In[9]:


#4. Convert the string into a list.


# In[10]:


lista =speech.split ()


# In[11]:


print (lista)


# In[12]:


#5. Use a dictionary to get the list of words and their frequencies.


# In[13]:


dictofWords ={i:lista [i]for i in range (0, len (lista))}


# In[14]:


print (dictofWords)


# In[15]:


#6. Sort the dictionary alphabetically.


# In[16]:


lista.sort ()


# In[17]:


lista


# In[18]:


#7. How many words does the text have?


# In[19]:


len (speech)


# In[20]:


#8. What is the most frequent word?


# In[21]:


def most_frequent(lista): 
    return max(set(lista), key = lista.count) 


# In[22]:


print (most_frequent(lista))


# In[23]:


#9. Sort the words from the most frequent to the least frequent.


# In[24]:


lista.sort (key =len)


# In[25]:


lista


# In[26]:


#10. How many words have appeared more than 50 times in the text?


# In[27]:


novalista= lista.split ()
wordfreq = []
for w in novalista:
    wordfreq.append (novalista.count (w))

