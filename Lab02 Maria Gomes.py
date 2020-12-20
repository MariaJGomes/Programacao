#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Construct a list (shoppingList) including 'potatoes', 'carrots', 'cod' and 'sprouts’


# In[2]:


shoppingList =list(('potatoes','carrots','cod','sprouts'))


# In[ ]:


#2) Get the second and the last element of the list


# In[3]:


shoppingList[0]


# In[4]:


shoppingList[-1]


# In[ ]:


#3) Iterate though the list


# In[5]:


for purchase in shoppingList:
    print(purchase)


# In[ ]:


#4) Create a new list (studentList)


# In[6]:


studentList=[ ]


# In[ ]:


#5) Add the follwoing elements to the shoppingList: orange and lime


# In[7]:


shoppingList.append('orange')


# In[8]:


shoppingList.append('lime')


# In[9]:


print (shoppingList)


# In[ ]:


#6) Remove the carrots, the first element and last element of the shoppingList list


# In[10]:


shoppingList.remove('carrots')


# In[11]:


shoppingList.pop()


# In[12]:


del shoppingList[0]


# In[13]:


print(shoppingList)


# In[ ]:


#7) Delete the shoppingList list


# In[14]:


del shoppingList


# In[ ]:


#8) Create a list with the double values of all integer number between 1 and 15.


# In[19]:


List = [x**2 for x in range(1,15)]


# In[20]:


print (List)


# In[ ]:


#9) Obtain the first 3 elements of the list


# In[21]:


firstThree = List[:3]


# In[22]:


print (firstThree)


# In[ ]:


#10) What is the result of, Why?


# In[20]:


shopping = shoppingList


# In[21]:


shoppingListCopy=shoppingList[:]


# In[22]:


print (shopping)


# In[ ]:


#12) What is the result of, Why?


# In[23]:


shopping = shoppingList


# In[24]:


shoppingList.append ('orange')


# In[25]:


print (shopping)


# In[ ]:


#13) Remove all the items from the shoppingList


# In[1]:


shoppingList=list (('potatoes','carrots','cod', 'sprouts', 'orange', 'lime'))


# In[2]:


shoppingList.clear ()


# In[3]:


print (shoppingList)


# In[ ]:


#14) What is the result of, Why?


# In[11]:


newpurchases=('bananas','beans', 'rice')


# In[13]:


print (newpurchases [1])


# In[15]:


newpurchases [0]='apple'


# In[ ]:


#15) Create a dictionary including the follwoing elements: orange, apple, pear, grape and peach. Key are 1 to 5. Iterate through key-value pair.


# In[4]:


fruit = {1: 'orange', 2:'apple', 3: 'pear', 4:'grape', 5:'peach'}


# In[5]:


for key, value in fruit.items():
    print ('The fruit' + str(key) + ' is ' + value)


# In[ ]:


#16) Create a weekList that is composed of several lists, each one corresponding to a day.


# In[7]:


weekList = [('monday'),('tuesday'), ('wednesday'), ('thursday'), ('friday')]


# In[8]:


print (weekList)

