#!/usr/bin/env python
# coding: utf-8

# In[1]:


moviesSeanConnery=["Dr. No (2962)", "From Russia with Love (1963)", "Goldfinger (1964)", "Thunderball (1965)", "You Only Live Twice (1967)", "Diamonds Are Forever (1971)", "Never Say Never Again (1983)"]


# In[2]:


moviesDavidNeven = ["Casino Royal (1967)"]


# In[3]:


moviesGeorgeLazenby =["On Her Majesty's Secret Service (1969)"]


# In[4]:


moviesRogerMoore = ["Live and Let Die (1973)", "The Man with the Golden Gun (1974)", "The Spy Who Loved Me (1977)", "Moonraker (1979)", "For Your Eyes Only (1981)", "A View to Kill (1985)" ]


# In[5]:


moviesTimothyDalton =["The Living Daylights (1987)", "Licence to kill (1989)"]


# In[6]:


moviesPierceBrosnan = ["GoldenEye (1995)", "Tomorrow Never Dies (1997)", "The World Is Not Enough (1999)", "Die Another Day (2002)"]


# In[7]:


moviesDanielCraig = ["Casino Royal (2006)", "Quantum of Solace (2008)", "Skyfall (2012)", "Spectre (2015)"]


# In[8]:


#1) Create a list of lists (movies007). The list will be composed by each list of movies featured by each actor.


# In[9]:


a = [moviesSeanConnery]


# In[10]:


b = [moviesDavidNeven]


# In[11]:


c = [moviesRogerMoore]


# In[12]:


d = [moviesTimothyDalton]


# In[13]:


e = [moviesPierceBrosnan]


# In[14]:


f = [moviesDanielCraig]


# In[15]:


g= [moviesGeorgeLazenby]


# In[16]:


movies007 = [a, b, c, d, e, f, g]


# In[17]:


print (movies007)


# In[18]:


#2) How many movies were played by the first actor to play James Bond?


# In[19]:


len (moviesSeanConnery)


# In[20]:


#3) How many movies were played by the last actor to play James Bond?


# In[21]:


len (moviesDanielCraig)


# In[22]:


#4) How many actors played the role of James Bond?


# In[23]:


len (movies007)


# In[24]:


#5) Create a new list with the number of movies played by each actor


# In[25]:


a= len(moviesSeanConnery)


# In[26]:


b= len(moviesDavidNeven) 


# In[27]:


c= len(moviesGeorgeLazenby)


# In[28]:


d= len (moviesRogerMoore)


# In[29]:


e = len (moviesTimothyDalton)


# In[30]:


f= len (moviesPierceBrosnan)


# In[31]:


g= len (moviesDanielCraig)


# In[34]:


List = [a, b, c, d, e, f, g]


# In[35]:


print (List)


# In[36]:


#6) How many movies were played by the actor who appeared most often in movies?


# In[37]:


List[0]


# In[38]:


#7) How many movies were played by the actor who appeared in fewer movies?


# In[39]:


List[1]


# In[40]:


#8) Create a new list (movies007a) with all the films.


# In[41]:


movies007a= [ ]
movies007a.extend (moviesSeanConnery)
movies007a.extend (moviesDavidNeven)
movies007a.extend (moviesGeorgeLazenby)
movies007a.extend (moviesRogerMoore)
movies007a.extend (moviesPierceBrosnan)
movies007a.extend (moviesDanielCraig)


# In[42]:


print (movies007a)


# In[43]:


#9) Sort the elements of the list


# In[44]:


movies007a.sort()


# In[45]:


print (movies007a)


# In[46]:


#9) Reverse the order of the list. What will happen if this method is executed twice? Does this method sort the list if it is not sorted?


# In[47]:


movies007a.reverse()


# In[48]:


print (movies007a)


# In[49]:


#10) What is the index of the movie "Spectre (2015)" in the list of movies


# In[50]:


print (movies007a.index("Spectre (2015)"))


# In[51]:


#11) Add the movie "007 and the bad Guy of the climate change (2020)" in the 11th position.


# In[52]:


movies007a.insert(10,"007 and the bad Guy of the climate change (2020)")


# In[53]:


print (movies007a)


# In[54]:


#12) It was a mistake. Remove the movie "007 and the bad Guy of the climate change (2020)"


# In[55]:


movies007a.remove("007 and the bad Guy of the climate change (2020)")


# In[56]:


print (movies007a)

